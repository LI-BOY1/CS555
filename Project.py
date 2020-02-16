import datetime
from prettytable import PrettyTable


# Cite: use the Project02 code from Professor's python answer

personList = []
familyList = []

flag = -1
birth = False
death = False
marry = False
div = False

class Person():

    def _init_(self):
        self.id = ''
        self.name = ""
        self.gender = ""
        self.birthDate = ""
        self.age = -1
        self.alive = True
        self.death = "NA"
        self.child = []
        self.spouse = []

class Family():

    def __init__(self):
        self.id = ''
        self.married = ''
        self.divorce = 'NA'
        self.husbandID = ''
        self.husbandName = ''
        self.wifeID = ''
        self.wifeName = ''
        self.chidren = []


def process_line(line):

    global flag, birth, death, marry, div, personList, familyList
    valid_tages = {
        '0': ('HEAD', 'NOTE', 'TRLR'),
        '1': ('BIRT', 'CHIL', 'DEAT', 'DIV', 'FAMC', 'FAMS', 'HUSB', 'MARR', 'NAME', 'SEX', 'WIFE'),
        '2': ('DATE')}

    # print(f"-->{line}")

    tokens = line.split()

    if len(tokens) == 3 and tokens[0] == '0' and tokens[2] in ('INDI', 'FAM'):
        level, args, tag = tokens
        valid = 'Y'

        #set the person flag
        if tokens[2] == 'INDI':
            flag = 0
            person = Person()


            # print(f"-->{line}")


            person.id = tokens[1]
            person.child = []
            person.spouse = []
            personList.append(person)

            # attrs = vars(person)
            # print(',  '.join("%s: %s" % item for item in attrs.items()))


        else:
            flag = 1
            family = Family();
            family.id = tokens[1]
            family.chidren = []

            familyList.append(family)

    elif len(tokens) >= 2:
        level, tag, args = tokens[0], tokens[1], " ".join(tokens[2:])
        valid = 'Y' if level in valid_tages and tag in valid_tages[level] else 'N'

        if(valid == 'Y'):

            if(level == "2"):
                if(birth):
                    birth = False
                    personList[-1].birthDate = args

                if(death):
                    death = False
                    personList[-1].death = args
                    personList[-1].alive = False
                else:
                    personList[-1].death = 'NA'
                    personList[-1].alive = True

                if(marry):
                    marry = False
                    familyList[-1].married = args

                if(div):
                    div = False
                    familyList[-1].divorce = args

            # deal with person
            if(flag == 0):
                if tokens[1] == "NAME":
                    personList[-1].name = args
                elif tokens[1] == "SEX":
                    personList[-1].gender = args
                elif tokens[1] == "BIRT":

                    birth = True
                elif tokens[1] ==  "DEAT":

                    death = True
                elif tokens[1] == "FAMC":
                    personList[-1].child.append(args)

                elif tokens[1] == "FAMS":
                    personList[-1].spouse.append(args)
            # deal wiht family
            else:
                if(tokens[1] == "MARR"):

                    marry = True
                elif (tokens[1] == "DIV"):

                    div = True
                elif ( tokens[1] == "HUSB"):
                    familyList[-1].husbandID = args
                elif (tokens[1] == "WIFE"):
                    familyList[-1].wifeID = args
                elif (tokens[1] == "CHIL"):
                    familyList[-1].chidren.append(args)


    else:
        level, tag, valid, args = tokens, "NA", 'N', 'NA'

    # print(f"<-- {level}|{tag}|{valid}|{args}")


def main():
    file = "/Users/boyli/Desktop/CS555-HW3/Boyang Li.ged"

    try:
        fp = open(file);
    except FileNotFoundError:
        print("Can't open your ", file)
    else:
        with fp:
            for line in fp:
                process_line(line.strip())

    global flag, birth, death, marry, div, personList, familyList

    now = datetime.datetime.now();
    year = now.year

    # calculate the age for each person
    for p in personList:
        birthdate = p.birthDate
        birthYear = birthdate.split()[2]
        age = year - int(birthYear)
        p.age = age

    #set the names
    for f in familyList:
        husId = f.husbandID
        wifeId = f.wifeID
        for p in personList:
            if(husId == p.id):
                f.husbandName = p.name
            if(wifeId == p.id):
                f.wifeName = p.name

    # sort the lists
    personList.sort(key=lambda p: p.id)
    familyList.sort(key=lambda f: f.id)



    # for p in personList:
    #     attrs = vars(p)
    #     print(',  '.join("%s: %s" % item for item in attrs.items()))

    # for f in familyList:
    #     attrs = vars(f)
    #     print(',  '.join("%s: %s" % item for item in attrs.items()))


    # create table
    pplTable = PrettyTable(['Id', 'Child', 'Spouse', 'Name', 'Gender', 'BirthDate', 'death', 'alive', 'Age'])
    famTable = PrettyTable(['Id', 'Married', 'divorce', 'HusbandID', 'HusbandName', 'WifeID', 'WifeName', 'Chidren'])

    for p in personList:
        list = []
        attrs = vars(p)
        for item in attrs.items():
            list.append(item[1])

        pplTable.add_row(list)


    for f in familyList:
        listf = []
        attrs = vars(f)
        for item in attrs.items():
            listf.append(item[1])

        famTable.add_row(listf)


    print(famTable)
    print()
    print(pplTable)

    famContent = famTable.get_string()
    pplContent = pplTable.get_string()
    with open('output.txt', 'w') as file:
        file.write(pplContent)
        file.write('\n')
        file.write(famContent)







if __name__ == '__main__':
    main()

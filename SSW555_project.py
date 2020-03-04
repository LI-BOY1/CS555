"""
This is the integrated code of SSW555 GEDCOM project.
All user stories will be included in this file.

Team member: Tianchen Xu, Qinlan Weng, Boyang, Li, Zeyu Wu

Sprint1 finish
US01 author @
US02 author @qw
US03 author @qw
US04 author @
US05 author @
US06 author @
US07 author @
US08 author @

Sprint Coding

"""



import datetime
from prettytable import PrettyTable

###############################################
#                                             #
#                 Parser                      #
#                 author @bl                  #
#                                             #
###############################################

# Cite: use the Project02 code from Professor's python answer

personList = []
familyList = []
sprint1output = "Sprint1Output.txt"

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
            family = Family()
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
                #     print(personList[-1].death)
                # else:
                #     personList[-1].death = 'N/A'
                #     personList[-1].alive = True

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


def createTable():
    global flag, birth, death, marry, div, personList, familyList

    now = datetime.datetime.now()
    year = now.year

    for p in personList:
        if not hasattr(p, 'death'):
            p.death = "N/A"
            p.alive = True

    # calculate the age for each person
    for p in personList:
        birthdate = p.birthDate
        birthYear = birthdate.split()[2]
        age = year - int(birthYear)
        p.age = age

    # set the names
    for f in familyList:
        husId = f.husbandID
        wifeId = f.wifeID
        for p in personList:
            if (husId == p.id):
                f.husbandName = p.name
            if (wifeId == p.id):
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
    #print()

    #famContent = famTable.get_string()
    #pplContent = pplTable.get_string()



###################### Parser end #########################


###############################################
#                                             #
#                 US 02                       #
#                 author @qw                  #
#                                             #
###############################################

def str_to_date(str_date):
    return datetime.datetime.strptime(str_date, '%d %b %Y').date()

def compare_date(date1, date2):
    """
    by qw
    """
    c_date1 = str_to_date(date1)
    c_date2 = str_to_date(date2)
    if c_date1 > c_date2:
        return 1
    elif c_date1 < c_date2:
        return -1
    else:
        return 0


def US02(personList, familyList, print_flag=True):
    """
    by qw
    To check if there is any violation of "Birth should occur before marriage of an individual"
    
    print_flag: boolean, whether the function print or not 
    """
    error = 0
    for f in familyList:
        for p in personList:

            if p.id == f.wifeID:
                if compare_date(p.birthDate, f.married) == 1:
                    error += 1
                    if print_flag:
                        print("ERROR: FAMILY: US02: " + f.id + " Wife's birth date " + str(str_to_date(p.birthDate)) + " following marriage date " + str(str_to_date(f.married)))

            if p.id == f.husbandID:
                if compare_date(p.birthDate, f.married) == 1:
                    error += 1
                    if print_flag:
                            print("ERROR: FAMILY: US02: " + f.id + " Husband's birth date " + str(str_to_date(p.birthDate)) + " following marriage date " + str(str_to_date(f.married)))
                            
    return error   


###############################################
#                                             #
#                 US 03                       #
#                 author @qw                  #
#                                             #
###############################################


def US03(personList, print_flag=True):
    """
    by qw
    To check if there is any violation of "Birth should occur before death of an individual"

    print_flag: boolean, whether the function print or not 
    """
    error = 0
    for p in personList:
        if p.death == "N/A":
            continue

        if compare_date(p.birthDate, p.death) == 1:
            error += 1
            if print_flag:
                print("ERROR: INDIVIDUAL: US03: " + p.id + " Died " + str(str_to_date(p.death)) + " before born " + str(str_to_date(p.birthDate)))

    return error   







###############################################
#                                             #
#                 US 04 05                    #
#                 author @bl                  #
#                                             #
###############################################


def US0405():

    # for f in familyList:
    #     attrs = vars(f)
    #     print(',  '.join("%s: %s" % item for item in attrs.items()))

    for f in familyList:
        if f.divorce == "NA":
            continue

        # check if the marry date is before divorce date
        divDate = datetime.datetime.strptime(f.divorce, '%d %b %Y').strftime("%Y-%m-%d")
        marDate = datetime.datetime.strptime(f.married, '%d %b %Y').strftime("%Y-%m-%d")
        res = ""

        if(marDate > divDate):
            print("marriage date " + marDate + " for family " + f.id + " is not before divorce date " + divDate)



    for p in personList:
        if p.alive == True:
            continue
        if p.spouse == []:
            continue

        # this person is dead and has spouse, then check if their marry date is before his/her death date
        deathDate = datetime.datetime.strptime(p.death, '%d %b %Y').strftime("%Y-%m-%d")

        for f in familyList:
            if f.husbandID == p.id or f.wifeID == p.id:
                marrydate = datetime.datetime.strptime(f.married, '%d %b %Y').strftime("%Y-%m-%d")
                if deathDate < marrydate:
                    print("marriage date " + marrydate + " for family " + f.id + " is not before death date " + deathDate + " for person " + p.id)





###############################################
#                                             #
#                 main                        #
#                                             #
#                                             #
###############################################


def main():
    
    #prepare data
    gedcom_file = "Springt01.ged"

    try:
        fp = open(gedcom_file)
    except FileNotFoundError:
        print("Can't open your ", gedcom_file)
    else:
        with fp:
            for line in fp:
                process_line(line.strip())

    createTable()

    #sprint1

    US02(personList, familyList)
    US03(personList)    
    US0405()


if __name__ == '__main__':
    main()

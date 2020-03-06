"""
This is the integrated code of SSW555 GEDCOM project.
All user stories will be included in this file.

Team member: Tianchen Xu, Qinlan Weng, Boyang, Li, Zeyu Wu

Sprint1 finish
US01 author @zw
US02 author @qw
US03 author @qw
US04 author @bl
US05 author @bl
US06 author @zw
US07 author @tx
US08 author @tx

Sprint2 Coding
US12 author @zw
US16 author @zw
"""

import datetime
from prettytable import PrettyTable
from collections import defaultdict
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


class Person:

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


class Family:

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

        # set the person flag
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

        if valid == 'Y':

            if level == "2":
                if (birth):
                    birth = False
                    personList[-1].birthDate = args

                if death:
                    death = False
                    personList[-1].death = args
                    personList[-1].alive = False
                #     print(personList[-1].death)
                # else:
                #     personList[-1].death = 'N/A'
                #     personList[-1].alive = True

                if marry:
                    marry = False
                    familyList[-1].married = args

                if div:
                    div = False
                    familyList[-1].divorce = args

            # deal with person
            if flag == 0:
                if tokens[1] == "NAME":
                    personList[-1].name = args
                elif tokens[1] == "SEX":
                    personList[-1].gender = args
                elif tokens[1] == "BIRT":

                    birth = True
                elif tokens[1] == "DEAT":

                    death = True
                elif tokens[1] == "FAMC":
                    personList[-1].child.append(args)

                elif tokens[1] == "FAMS":
                    personList[-1].spouse.append(args)

            # deal wiht family
            else:
                if tokens[1] == "MARR":

                    marry = True
                elif tokens[1] == "DIV":

                    div = True
                elif tokens[1] == "HUSB":
                    familyList[-1].husbandID = args
                elif tokens[1] == "WIFE":
                    familyList[-1].wifeID = args
                elif tokens[1] == "CHIL":
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
            if husId == p.id:
                f.husbandName = p.name
            if wifeId == p.id:
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
    # print()

    # famContent = famTable.get_string()
    # pplContent = pplTable.get_string()

    famContent = famTable.get_string()
    pplContent = pplTable.get_string()
    with open(sprint1output, 'w') as file:
        file.write(pplContent)
        file.write('\n')
        file.write(famContent)
        file.write('\n')





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

                        res = "ERROR: FAMILY: US02: " + f.id + " Wife's birth date " + str(
                              str_to_date(p.birthDate)) + " following marriage date " + str(str_to_date(f.married))

                        print(res)

                        with open(sprint1output, 'a') as file:
                            file.write(res)
                            file.write('\n')

            if p.id == f.husbandID:
                if compare_date(p.birthDate, f.married) == 1:
                    error += 1
                    if print_flag:
                        res = "ERROR: FAMILY: US02: " + f.id + " Husband's birth date " + str(
                            str_to_date(p.birthDate)) + " following marriage date " + str(str_to_date(f.married))
                        print(res)
                        with open(sprint1output, 'a') as file:
                            file.write(res)
                            file.write('\n')

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

                res = "ERROR: INDIVIDUAL: US03: " + p.id + " Died " + str(str_to_date(p.death)) + " before born " + str(
                    str_to_date(p.birthDate))

                print(res)

                with open(sprint1output, 'a') as file:
                    file.write(res)
                    file.write('\n')

    return error


###############################################
#                                             #
#                 US 04 05                    #
#                 author @bl                  #
#                                             #
###############################################


def US0405(familyList, personList):
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

        if (marDate > divDate):
            res = "ERROR: FAMILY: US04: marriage date " + marDate + " for family " + f.id + " is not before divorce date " + divDate

        print(res);

        with open(sprint1output, 'a') as file:
            file.write(res)
            file.write('\n')

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
                    with open(sprint1output, 'a') as file:
                        res = "ERROR: FAMILY: US05: marriage date " + marrydate + " for family " + f.id + " is not before death date " + deathDate + " for person " + p.id
                        print(res)
                        file.write(res)
                        file.write('\n')

###############################################
#                                             #
#                 US 01                       #
#                 author @zw                  #
#                                             #
###############################################


def us01(personList, familyList):
    """ Dates (birth, marriage, divorce, death) should not be after the current date """
    verify = True
    current_time = datetime.datetime.now().date()
    for person in personList:
        birth_date = datetime.datetime.strptime(datetime.datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
        if person.birthDate is not None and birth_date > datetime.datetime.now().date():
            res = "ERROR: INDIVIDUAL: US01: " + person.id + ": Birthday " + str(birth_date) + " occurs in the future"
            print(res)
            with open(sprint1output, 'a') as file:
                file.write(res)
                file.write('\n')

            verify = False
        if person.death != 'N/A':
            death = datetime.datetime.strptime(datetime.datetime.strptime(person.death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if death > current_time:
                res = "ERROR: INDIVIDUAL: US01: " + person.id + ": death " + str(death) + " occurs in the future"
                print(res)
                with open(sprint1output, 'a') as file:
                    file.write(res)
                    file.write('\n')

                verify = False

    for family_member in familyList:
        if family_member.married != 'N/A':
            marry_date = datetime.datetime.strptime(datetime.datetime.strptime(family_member.married, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if marry_date > current_time:
                res = "ERROR: FAMILY: US01: "+ family_member.husbandName + " and " + family_member.wifeName + " marry at " + str(marry_date) + ", in the future"
                print(res)
                with open(sprint1output, 'a') as file:
                    file.write(res)
                    file.write('\n')
                verify = False
        if family_member.divorce != 'NA':
            divorce_date = datetime.datetime.strptime(datetime.datetime.strptime(family_member.divorce, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if divorce_date > current_time:
                res = "ERROR: FAMILY: US01: " + family_member.husbandName + " and " + family_member.wifeName + " divorce at " + str(divorce_date) + ", in the future"
                print(res)
                with open(sprint1output, 'a') as file:
                    file.write(res)
                    file.write('\n')

                verify = False
    if verify:
        return "All dates happen before current date."
    else:
        return "Not all dates happen before current date."

###############################################
#                                             #
#                 US 06                       #
#                 author @zw                  #
#                                             #
###############################################


def us06(personList, familyList):
    """  Divorce can only occur before death of both spouses """
    verify = True
    for family in familyList:
        if family.divorce != 'NA':
            divorce_date = datetime.datetime.strptime(datetime.datetime.strptime(family.divorce, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            for i in range(len(personList)):
                if personList[i].id == family.husbandID:
                    if personList[i].death != 'N/A':
                        husband_death = datetime.datetime.strptime(datetime.datetime.strptime(personList[i].death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                if personList[i].id == family.wifeID:
                    if personList[i].death != 'N/A':
                        wife_death = datetime.datetime.strptime(datetime.datetime.strptime(personList[i].death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if divorce_date > husband_death:
                res = "ERROR: FAMILY: US06: " + family.id + ": Divorced " + str(divorce_date) + " after husband's (" + family.husbandID + ") death on " + str(husband_death)
                print(res)
                with open(sprint1output, 'a') as file:
                    file.write(res)
                    file.write('\n')

                verify = False
            if divorce_date > wife_death:
                res = "ERROR: FAMILY: US06: " + family.id + ": Divorced " + str(divorce_date) + " after wife's (" + family.wifeID + ") death on " + str(wife_death)
                print(res)
                with open(sprint1output, 'a') as file:
                    file.write(res)
                    file.write('\n')

                verify = False
    if verify:
        return "All divorces happen before one is dead."
    else:
        return "Not all divorces happen before one is dead."


###############################################
#                                             #
#                 US 07                       #
#                 author @tx                  #
#                                             #
###############################################

def us07(personList, familyList):
    # Less then 150 years old
    """
    Death less than 150 years after birth for dead people
    current date less than 150 years after birth for all living people
    """
    flag = True
    date_now = datetime.datetime.now().date()
    for person in personList:
        #check dead people
        if person.alive == False:
            # get death
            death_date = datetime.datetime.strptime(datetime.datetime.strptime(person.death,'%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            # get birth
            birth_date = datetime.datetime.strptime(datetime.datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            div_time = (death_date - birth_date).days/365.25
            if div_time > 150:
                res = "ERROR: INDIVIDUAL: US07: " + person.id + ": more than 150 years old"
                print(res)
                with open(sprint1output, 'a') as file:
                    file.write(res)
                    file.write('\n')

                flag = False
        else:
            # get birth
            birth_date = datetime.datetime.strptime(datetime.datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            div_time = (date_now - birth_date).days/365.25
            if div_time > 150:
                res = "ERROR: INDIVIDUAL: US07: " + person.id + ": more than 150 years old"
                print(res)
                with open(sprint1output, 'a') as file:
                    file.write(res)
                    file.write('\n')

                flag = False
    if flag:
        return 'Correct'
    else:
        return 'Error'


###############################################
#                                             #
#                 US 08                       #
#                 author @tx                  #
#                                             #
###############################################

def us08(personList, familyList):
    # Birth before marriage of parents
    """
    Children should be born after marriage of parents
    (and not more than 9 months after their divorce)
    """
    flag = True
    for person in personList:
        key = person.child
        ky = "".join(key)
        birth_date = datetime.datetime.strptime(datetime.datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
        for i in range(len(familyList)):
            if familyList[i].id == ky:
                married_date = datetime.datetime.strptime(datetime.datetime.strptime(familyList[i].married, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                if married_date > birth_date:
                    res = "ERROR: INDIVIDUAL: US08: " + person.id + ": birth before marriage"
                    print(res)
                    with open(sprint1output, 'a') as file:
                        file.write(res)
                        file.write('\n')
                    flag = False

                divorce = familyList[i].divorce
                if divorce != 'NA':
                    divorce_date = datetime.datetime.strptime(datetime.datetime.strptime(familyList[i].divorce, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                    dif_time = ((birth_date - divorce_date).days/365.25) * 12
                    # print(dif_time)
                    if dif_time > 9:
                        res = "ERROR: INDIVIDUAL: US08: " + person.id + ": birth before marriage"
                        print(res)
                        with open(sprint1output, 'a') as file:
                            file.write(res)
                            file.write('\n')
                        flag = False
    if flag:
        return "Correct"
    else:
        return "Error"
###############################################
#                                             #
#                 US 12                       #
#                 author @zw                  #
#                                             #
###############################################


def us12(personList, familyList):
    """ Mother should be less than 60 years older than her children and father should be less than 80 years older than his children """
    verify = True
    for family in familyList:
        if family.chidren:
            children_age = defaultdict(int)
            for person in personList:
                if person.id == family.husbandID:
                    father_age = person.age
                if person.id == family.wifeID:
                    mother_age = person.age

            for children in family.chidren:
                for person in personList:
                    if person.id == children:
                        children_age[person.id] = person.age
            for child in children_age.keys():
                if father_age - children_age[child] > 80:
                    print(f"ERROR: FAMILY: US12: {child}'s father is more than 80 years older than he. {father_age - children_age[child]} years older.")
                    verify = False
                if mother_age - children_age[child] > 60:
                    print(f"ERROR: FAMILY: US12: {child}'s mother is more than 60 years older than he. {mother_age - children_age[child]} years older.")
                    verify = False
                else:
                    continue
        else:
            verify = True
    if verify:
        return "All mothers are less than 60 years older than their children and all fathers are less than 80 years older than their children"
    else:
        return "Not all mothers are less than 60 years older than their children, or all fathers are less than 80 years older than their children"

###############################################
#                                             #
#                 US 16                       #
#                 author @zw                  #
#                                             #
###############################################


def us16(personList, familyList):
    """ All male members of a family should have the same last name """
    verify = True
    for family in familyList:
        if family.chidren:
            children_ltnm = defaultdict(str)
            for person in personList:
                if person.id == family.husbandID:
                    father_ltnm = person.name.split('/')[1]
            for children in family.chidren:
                for person in personList:
                    if person.id == children:
                        if person.gender == 'M':
                            children_ltnm[person.id] = person.name.split('/')[1]
            for child in children_ltnm.keys():
                if children_ltnm[child] != father_ltnm:
                    print(f"ERROR: FAMILY: US16: {child}'s last name is different from father's. Child's last name: {children_ltnm[child]}, father's last name: {father_ltnm}.")
                    verify = False
    if verify:
        return "All male members of a family have the same last name"
    else:
        return "Not all male members of a family have the same last name"
###############################################
#                                             #
#                 main                        #
#                                             #
#                                             #
###############################################


def main():
    # prepare data
    gedcom_file = "Qinlan Weng.ged"

    try:
        fp = open(gedcom_file, encoding='UTF-8')
    except FileNotFoundError:
        print("Can't open your ", gedcom_file)
    else:
        with fp:
            for line in fp:
                process_line(line.strip())

    createTable()

    # sprint1

    US02(personList, familyList)
    US03(personList)
    US0405(familyList, personList)
    us01(personList, familyList)
    us06(personList, familyList)
    us07(personList, familyList)
    us08(personList, familyList)

    # sprint2

    us12(personList, familyList)
    us16(personList, familyList)


if __name__ == '__main__':
    main()

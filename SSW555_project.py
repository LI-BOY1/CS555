"""
This is the integrated code of SSW555 GEDCOM project.
All user stories will be included in this file.

Team member: Tianchen Xu, Qinlan Weng, Boyang, Li, Zeyu Wu

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
sprint_output = "sprint04_output.txt"

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
    with open(sprint_output, 'w') as file:
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


def us02(personList, familyList):
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
                    res = "ERROR: FAMILY: US02: " + f.id + " Wife's birth date " + str(str_to_date(p.birthDate)) + " following marriage date " + str(str_to_date(f.married))
                    write_file_and_print(sprint_output, res)

            if p.id == f.husbandID:
                if compare_date(p.birthDate, f.married) == 1:
                    error += 1
                    res = "ERROR: FAMILY: US02: " + f.id + " Husband's birth date " + str(str_to_date(p.birthDate)) + " following marriage date " + str(str_to_date(f.married))
                    write_file_and_print(sprint_output, res)

    return error


###############################################
#                                             #
#                 US 03                       #
#                 author @qw                  #
#                                             #
###############################################


def us03(personList):
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
            res = "ERROR: INDIVIDUAL: US03: " + p.id + " Died " + str(str_to_date(p.death)) + " before born " + str(str_to_date(p.birthDate))
            write_file_and_print(sprint_output, res)
 
    return error


###############################################
#                                             #
#                 US 04 05                    #
#                 author @bl                  #
#                                             #
###############################################


def us0405(familyList, personList):
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

        print(res)

        with open(sprint_output, 'a') as file:
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
                    with open(sprint_output, 'a') as file:
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
        try:
            birth_date = datetime.datetime.strptime(datetime.datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
        except ValueError:
            pass
        else:
            if person.birthDate is not None and birth_date > datetime.datetime.now().date():
                res = "ERROR: INDIVIDUAL: US01: " + person.id + ": Birthday " + str(birth_date) + " occurs in the future"
                write_file_and_print(sprint_output, res)
                verify = False
        if person.death != 'N/A':
            try:
                death = datetime.datetime.strptime(datetime.datetime.strptime(person.death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            except ValueError:
                pass
            else:
                if death > current_time:
                    res = "ERROR: INDIVIDUAL: US01: " + person.id + ": death " + str(death) + " occurs in the future"
                    write_file_and_print(sprint_output, res)
                    verify = False

    for family_member in familyList:
        if family_member.married != 'N/A':
            marry_date = datetime.datetime.strptime(datetime.datetime.strptime(family_member.married, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if marry_date > current_time:
                res = "ERROR: FAMILY: US01: " + family_member.husbandName + " and " + family_member.wifeName + " marry at " + str(marry_date) + ", in the future"
                write_file_and_print(sprint_output, res)
                verify = False
        if family_member.divorce != 'NA':
            divorce_date = datetime.datetime.strptime(datetime.datetime.strptime(family_member.divorce, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if divorce_date > current_time:
                res = "ERROR: FAMILY: US01: " + family_member.husbandName + " and " + family_member.wifeName + " divorce at " + str(divorce_date) + ", in the future"
                write_file_and_print(sprint_output, res)
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
                write_file_and_print(sprint_output, res)
                verify = False
            if divorce_date > wife_death:
                res = "ERROR: FAMILY: US06: " + family.id + ": Divorced " + str(divorce_date) + " after wife's (" + family.wifeID + ") death on " + str(wife_death)
                write_file_and_print(sprint_output, res)
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
            try:
                # get death
                death_date = datetime.datetime.strptime(datetime.datetime.strptime(person.death,'%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                # get birth
                birth_date = datetime.datetime.strptime(datetime.datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            except ValueError:
                pass
            else:
                div_time = (death_date - birth_date).days/365.25
                if div_time > 150:
                    res = "ERROR: INDIVIDUAL: US07: " + person.id + ": more than 150 years old"
                    print(res)
                    with open(sprint_output, 'a') as file:
                        file.write(res)
                        file.write('\n')

                    flag = False
        else:
            try:
                # get birth
                birth_date = datetime.datetime.strptime(datetime.datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            except ValueError:
                pass
            else:
                div_time = (date_now - birth_date).days/365.25
                if div_time > 150:
                    res = "ERROR: INDIVIDUAL: US07: " + person.id + ": more than 150 years old"
                    print(res)
                    with open(sprint_output, 'a') as file:
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
                    with open(sprint_output, 'a') as file:
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
                        with open(sprint_output, 'a') as file:
                            file.write(res)
                            file.write('\n')
                        flag = False
    if flag:
        return "Correct"
    else:
        return "Error"   

###############################################
#                                             #
#                 US 09                       #
#                 author @xt                  #
#                                             #
###############################################
def us09(personList, familyList):
    # Birth before death of parents
    """Child should be born before death of mother and before 9 months after death of father"""
    flag = True
    for family in familyList:
        child_key = "".join(family.chidren)
        hus_key = family.husbandID
        wf_key = family.wifeID

        for i in range(len(personList)):
            if personList[i].id == child_key:
                try:
                    child_birth = datetime.datetime.strptime(datetime.datetime.strptime(personList[i].birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                except ValueError:
                    pass
                else:    
                    # check wf/child
                    for person in personList:
                        if person.id == wf_key:
                            if person.death != "N/A":
                                try:
                                    wf_death = datetime.datetime.strptime(datetime.datetime.strptime(person.death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                                except ValueError:
                                    pass
                                else:
                                    if wf_death < child_birth:
                                        res = "ERROR: INDIVIDUAL: US09: " + child_key + ": birth before death of " + wf_key
                                        write_file_and_print(sprint_output, res)
                                        flag = False
                    # check hus/child
                    for person in personList:
                        if person.id == hus_key:
                            if person.death != "N/A":
                                try:
                                    hus_death = datetime.datetime.strptime(datetime.datetime.strptime(person.death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                                except ValueError:
                                    pass
                                else:
                                    dif_time = ((child_birth - hus_death).days/365.25) * 12
                                    if dif_time > 9:
                                        res = "ERROR: INDIVIDUAL: US09: " + child_key + ": birth 9 months after death of " + hus_key
                                        write_file_and_print(sprint_output, res)
                                        flag = False
    if flag:
        return "Correct"
    else:
        return "Error"

###############################################
#                                             #
#                 US 10                       #
#                 author @tx                  #
#                                             #
###############################################
def us10(personList, familyList):
    # Marriage after 14
    """Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)"""
    flag = True
    for person in personList:
        # print(person.spouse)
        if person.spouse != []:
            if person.age < 14:
                res = "ERROR: INDIVIDUAL: US10: " + person.id + ": Marriage after 14"
                write_file_and_print(sprint_output, res)
                flag = False
    if flag:
        return "Correct"
    else:
        return "Error"
    
###############################################
#                                             #
#                 US 15                       #
#                 author @qw                  #
#                                             #
###############################################

def write_file_and_print(file_name, res):
    print(res)
    with open(file_name, 'a') as file:
        file.write(res)
        file.write('\n')


def us15(familyList):
    """
    by qw
    us 15 Fewer than 15 siblings
    To check if there is any violation of "There should be fewer than 15 siblings in a family"
    """

    error = 0
    for f in familyList:
        sibling_cnt = len(f.chidren)
        if sibling_cnt >= 15:
            error += 1
            res = "ERROR: FAMILY: US15: family " + str(f.id) + " has " + str(sibling_cnt) + " children"
            write_file_and_print(sprint_output, res)

    return error




###############################################
#                                             #
#                 US 18                       #
#                 author @qw                  #
#                                             #
###############################################

def us18(familyList):
    """
    by qw
    us 18 Siblings should not marry
    To check if there is any violation of "Siblings should not marry one another"
    """

    error = 0
    for f1 in familyList:
        for f2 in familyList:
            if f2.husbandID in f1.chidren and f2.wifeID in f1.chidren:
                error += 1
                res = "ERROR: FAMILY: US18: In family " + str(f1.id) + " chird " + str(f2.husbandID) + " marries his sibling " + str(f2.wifeID)
                write_file_and_print(sprint_output, res)

    return error
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
                    res = "ERROR: FAMILY: US12: " + child + "'s father is more than 80 years older than he. " + str(father_age - children_age[child]) + " years older."
                    write_file_and_print(sprint_output, res)
                    verify = False

                if mother_age - children_age[child] > 60:
                    res = "ERROR: FAMILY: US12: " + child + "'s mother is more than 60 years older than he. " + str(mother_age - children_age[child]) + " years older."
                    write_file_and_print(sprint_output, res)
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
                    res = "ERROR: FAMILY: US16: " + child + "'s last name is different from father's. Child's last name: " + children_ltnm[child] + ", father's last name: " + father_ltnm + "."
                    write_file_and_print(sprint_output, res)
                    verify = False
    if verify:
        return "All male members of a family have the same last name"
    else:
        return "Not all male members of a family have the same last name"




###############################################
#                                             #
#                 US 22                       #
#                 author boyang Li            #
#                                             #
###############################################

def us22(personList, familyList):
    pset = set()
    fset = set()
    for p in personList:
        if p.id not in pset:
            pset.add(p.id)
        else:
            res = "ERROR: INDIVIDUAL: US22: person id " + p.id + " is duplicated"
            write_file_and_print(sprint_output, res)

    for f in familyList:
        if f.id not in fset:
            fset.add(f.id)
        else:
            res = "ERROR: FAMILY: US22: family id " + f.id + " is duplicated"
            write_file_and_print(sprint_output, res)

###############################################
#                                             #
#                 US 23                       #
#                 author boyang Li            #
#                                             #
###############################################

def us23(personList):
    pset = set()
    for p in personList:
        iden = p.name + " " + p.birthDate
        if iden not in pset:
            pset.add(iden)
        else:
            res = "ERROR: INDIVIDUAL: US23: more than one person has the same birthday and name " + iden
            write_file_and_print(sprint_output, res)




###############################################
#                                             #
#                 US 24                       #
#                 author boyang li            #
#                                             #
###############################################
def us24(familyList):
    fset = set()

    for f in familyList:
        key = "" + f.married + "/" + f.husbandName + "/" + f.wifeName
        if key not in fset:
            fset.add(key)
        else:
            res = "ERROR: FAMILY: US24: family id " + f.id + " has the duplicated marry date " + f.married + "  and husband name " + f.husbandName + " and wfie name " + f.wifeName
            write_file_and_print(sprint_output, res)


###############################################
#                                             #
#                 US 25                       #
#                 author boyang li            #
#                                             #
###############################################
def us25(personList, familyList):
    fset = set()

    for f in familyList:
        list = f.chidren
        for ids in list:
            for p in personList:
                if ids == p.id:
                    iden = "" + p.name + "/" + p.birthDate
                    if iden not in fset:
                        fset.add(iden)
                    else:
                        res = "ERROR: FAMILY: US25: family id " + f.id + " has the children with same name " + p.name + "  and birthday " + p.birthDate
                        write_file_and_print(sprint_output, res)


###############################################
#                                             #
#                 US 21                       #
#                 author @zw                  #
#                                             #
###############################################


def us21(personList, familyList):
    """ Husband in family should be male and wife in family should be female """
    verify = True
    for family in familyList:
        for person in personList:
            if person.id == family.husbandID:
                if person.gender != 'M':
                    res = "ERROR: FAMILY: US21: " + person.id + "'s role in a family is husband, but the gender of " + person.id + "  is " + person.gender + "."
                    write_file_and_print(sprint_output, res)
                    verify = False
            if person.id == family.wifeID:
                if person.gender != "F":
                    res = "ERROR: FAMILY: US21: " + person.id + "'s role in a family is wife, but the gender of " + person.id + " is " + person.gender + "."
                    write_file_and_print(sprint_output, res)
                    verify = False
    if verify:
        return "Husband in family is male and wife in family is female"
    else:
        return "Husband in family is not male or wife in family is not female"


###############################################
#                                             #
#                 US 27                       #
#                 author @qw                  #
#                                             #
###############################################


def us27(familyList):
    """
    by qw
    us 27 Include individual ages
    To "Include person's current age when listing individuals"
    """
    pass
    # age is already included in the original individuals pretty table


###############################################
#                                             #
#                 US 28                       #
#                 author @qw                  #
#                                             #
###############################################
def us28(personList, familyList):
    """
    by qw
    us 28 Order siblings by age
    List siblings in families by decreasing age, i.e. oldest siblings first
    """
    
    test_lst = []
    
    for f in familyList:
        if f.chidren == []:
            continue
        
        children_b_date = []
        for child in  f.chidren:
            b_date = str_to_date('1 JAN 9999')
            
            for p in personList:
                if child == p.id:
                    b_date = str_to_date(p.birthDate)

            children_b_date.append((child, b_date))
        
        children_b_date = sorted(children_b_date, key=lambda x:x[1])
        
        #print(children_b_date)

        f.chidren = [x[0] for x in children_b_date]
        test_lst.append(f.chidren)
    
    #print(test_lst)
    return familyList 

        


   


###############################################
#                                             #
#                 US 29                       #
#                 author @zw                  #
#                                             #
###############################################


def us29(personList):
    """ List all deceased individuals in a GEDCOM file """
    deceased_list = []
    deceasedTable = PrettyTable(['ID', 'name', 'birth date', 'death date'])
    for person in personList:
        if not person.alive:
            deceased_list.append(person.id)
            deceasedTable.add_row([person.id, person.name, person.birthDate, person.death])
    res = "us29: Deceased Individuals"
    write_file_and_print(sprint_output, res)
    tableConten = deceasedTable.get_string()
    write_file_and_print(sprint_output, tableConten)

    return deceased_list

###############################################
#                                             #
#                 US 30                       #
#                 author @tx                  #
#                                             #
###############################################

def us30(personList):
    # List living married
    """List all living married people in a GEDCOM file"""
    living_married_list = []
    living_married_table = PrettyTable(['ID', 'name', 'BirthDate', 'death'])
    for person in personList:
        if person.spouse != [] and person.alive == True:
            living_married_list.append(person.id)
            living_married_table.add_row([person.id, person.name, person.birthDate, person.death])

    res = "us30: List living married"
    write_file_and_print(sprint_output, res)
    tableContent = living_married_table.get_string()
    write_file_and_print(sprint_output, tableContent)

    return living_married_list

###############################################
#                                             #
#                 US 31                       #
#                 author @tx                  #
#                                             #
###############################################

def us31(personList):
    # List living single
    """List all living people over 30 who have never been married in a GEDCOM file"""
    living_single_list = []
    living_single_table = PrettyTable(['ID', 'name', 'BirthDate', 'death'])
    for person in personList:
        if person.spouse == [] and person.age > 30 and person.alive == True:
            living_single_list.append(person.id)
            living_single_table.add_row([person.id, person.name, person.birthDate, person.death])


    res = "us31: List living single"
    write_file_and_print(sprint_output, res)

    tableContent = living_single_table.get_string()
    write_file_and_print(sprint_output, tableContent)

    return living_single_list

###############################################
#                                             #
#                 US 34                       #
#                 author @zw                  #
#                                             #
###############################################


def us34(personList, familyList):
    """ List all couples who were married when the older spouse was more than twice as old as the younger spouse """
    verify = True
    checkTable = PrettyTable(['ID', 'married', 'age when husband was married', 'age when wife was married'])
    for family in familyList:
        marry_date = datetime.datetime.strptime(family.married, '%d %b %Y').year
        for person in personList:
            if person.id == family.husbandID:
                birth_date_m = datetime.datetime.strptime(person.birthDate, '%d %b %Y').year
            if person.id == family.wifeID:
                birth_date_f = datetime.datetime.strptime(person.birthDate, '%d %b %Y').year

        if marry_date - birth_date_m > (marry_date - birth_date_f) * 2:
            res = f"ERROR: FAMILY: US34: In family {family.id}, husband was more than twice as old as the wife when they are married."
            write_file_and_print(sprint_output, res)
            checkTable.add_row([family.id, family.married, marry_date - birth_date_m, marry_date - birth_date_f])
            verify = False
        if marry_date - birth_date_f > (marry_date - birth_date_m) * 2:
            res = f"ERROR: FAMILY: US34: In family {family.id}, wife was more than twice as old as the husband when they are married."
            write_file_and_print(sprint_output, res)
            checkTable.add_row([family.id, family.married, marry_date - birth_date_m, marry_date - birth_date_f])
            verify = False
    print("us34: Couples who were married when the older spouse was more than twice as old as the younger spouse")
    print(checkTable)
    if verify:
        return "No couples who were married when the older spouse was more than twice as old as the younger spouse"
    else:
        return "There are some couples who were married when the older spouse was more than twice as old as the younger spouse"

###############################################
#                                             #
#                 US 38                       #
#                 author @tx                  #
#                                             #
###############################################

def us38(personList):
    # List upcoming birthdays
    """List all living people in a GEDCOM file whose birthdays occur in the next 30 days"""
    current_time = datetime.datetime.now().date()
    today_d = datetime.datetime.now()
    birth_coming_list =[]
    birth_coming_table = PrettyTable(['ID', 'name', 'BirthDate', 'death'])

    for person in personList:
        if person.alive == True:
            try:
                birth_date = datetime.datetime.strptime(datetime.datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            except ValueError:
                pass
            else:
                birth_this_year = birth_date.replace(year=today_d.year)
                div_day = (birth_this_year - current_time).days
                if 0 < div_day < 30: 
                    birth_coming_list.append(person.id)
                    birth_coming_table.add_row([person.id, person.name, person.birthDate, person.death])
    
    res = "us38: List upcoming birthdays"
    write_file_and_print(sprint_output, res)

    tableContent = birth_coming_table.get_string()
    write_file_and_print(sprint_output, tableContent)

    return birth_coming_list


###############################################
#                                             #
#                 US 39                       #
#                 author @tx                  #
#                                             #
###############################################

def us39(personList, familyList):
    # List upcoming anniversaries
    """List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days"""
    current_time = datetime.datetime.now().date()
    today_d = datetime.datetime.now()
    marriage_anvrsy_list = []
    marriage_anvrsy_table = PrettyTable(["ID", "Married", "divorce","HusbandID", "HusbandName", "WifeID", "WifeName"])

    for family in familyList:
        if family.divorce == "NA":
            try:
                married_date = datetime.datetime.strptime(datetime.datetime.strptime(family.married, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            except ValueError:
                pass
            else:
                # check hus
                hus_id = family.husbandID
                wif_id = family.wifeID
                for person in personList:
                    if person.id == hus_id and person.alive == True:
                        for p in personList:
                            if p.id == wif_id and p.alive == True:
                                married_this_year = married_date.replace(year=today_d.year)
                                div_day = (married_this_year - current_time).days
                                if 0 < div_day < 30: 
                                    marriage_anvrsy_list.append(family.id)
                                    marriage_anvrsy_table.add_row([family.id, family.married, family.divorce, family.husbandID, family.husbandName, family.wifeID, family.wifeName])
    
    res = "us39: List upcoming anniversaries"
    write_file_and_print(sprint_output, res)

    tableContent = marriage_anvrsy_table.get_string()
    write_file_and_print(sprint_output, tableContent)

    return marriage_anvrsy_list

###############################################
#                                             #
#                 US 42                       #
#                 author @zw                  #
#                                             #
###############################################


def us42(personList, familyList):
    """ All dates should be legitimate dates for the months specified (e.g., 2/30/2015 is not legitimate) """
    verify = True
    for family in familyList:
        try:
            datetime.datetime.strptime(family.married, '%d %b %Y').date()
        except ValueError:
            res = f"ERROR: FAMILY: US42: {family.id} was married at {family.married}, which is not legitimate."
            write_file_and_print(sprint_output, res)
            verify = False
        if family.divorce != "NA":
            try:
                datetime.datetime.strptime(family.divorce, '%d %b %Y').date()
            except ValueError:
                res = f"ERROR: FAMILY: US42: {family.id} was divorced at {family.divorce}, which is not legitimate."
                write_file_and_print(sprint_output, res)
                verify = False
    for person in personList:
        try:
            datetime.datetime.strptime(person.birthDate, '%d %b %Y').date()
        except ValueError:
            res = f"ERROR: INDIVIDUAL: US42: {person.id} was born at {person.birthDate}, which is not legitimate."
            write_file_and_print(sprint_output, res)
            verify = False
        if person.death != "N/A":
            try:
                datetime.datetime.strptime(person.death, '%d %b %Y').date()
            except ValueError:
                res = f"ERROR: FAMILY: US42: {person.id} died at {person.death}, which is not legitimate."
                write_file_and_print(sprint_output, res)
                verify = False
    if verify:
        return "All dates are legitimate dates for the months specified."
    else:
        return "Not all dates are legitimate dates for the months specified."



###############################################
#                                             #
#                 main                        #
#                                             #
#                                             #
###############################################


def main():
    global familyList
    # prepare data
    gedcom_file = "sprint04.ged"
    # MAKE SURE gedcom_file match sprint_output in the beginning of this file

    try:
        fp = open(gedcom_file, encoding='UTF-8')
    except FileNotFoundError:
        print("Can't open your ", gedcom_file)
    else:
        with fp:
            for line in fp:
                process_line(line.strip())

    familyList = us28(personList, familyList)

    createTable()

    # sprint1
    us01(personList, familyList)
    us02(personList, familyList)
    # us03(personList)
    # us0405(familyList, personList)
    us06(personList, familyList)
    us07(personList, familyList)
    us08(personList, familyList)
    
    # spirnt2
    us09(personList, familyList)
    us10(personList, familyList)
    us15(familyList)
    us18(familyList)
    us12(personList, familyList)
    us16(personList, familyList)
    us22(personList, familyList)
    us23(personList)
    
    # sprint3
    us24(familyList)
    us25(personList, familyList)
    us21(personList, familyList)
    us29(personList)
    us30(personList)
    us31(personList)

    # sprint4
    us34(personList, familyList)
    us42(personList, familyList)
    us38(personList)
    us39(personList, familyList)

if __name__ == '__main__':
    main()

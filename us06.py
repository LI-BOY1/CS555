import Project
from datetime import datetime


def us06():
    """  Divorce can only occur before death of both spouses """
    verify = True
    for family in Project.familyList:
        if family.divorce != 'NA':
            divorce_date = datetime.strptime(datetime.strptime(family.divorce, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            for i in range(len(Project.personList)):
                if Project.personList[i].id == family.husbandID:
                    if Project.personList[i].death != 'N/A':
                        husband_death = datetime.strptime(datetime.strptime(Project.personList[i].death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                if Project.personList[i].id == family.wifeID:
                    if Project.personList[i].death != 'N/A':
                        wife_death = datetime.strptime(datetime.strptime(Project.personList[i].death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if divorce_date > husband_death or divorce_date > wife_death:
                print(f"{family.husbandName} and {family.wifeName} divorced after one is dead.")
                verify = False
    if verify:
        return "All divorces happen before one is dead."
    else:
        return "Not all divorces happen before one is dead."


def main():
    """ run the code """
    Project.main()
    print(us06())


if __name__ == '__main__':
    main()
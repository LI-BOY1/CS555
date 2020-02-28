import Project
from datetime import datetime


def us01():
    """ Dates (birth, marriage, divorce, death) should not be after the current date """
    verify = True
    current_time = datetime.now().date()
    for person in Project.personList:
        birth_date = datetime.strptime(datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
        if person.birthDate is not None and birth_date > datetime.now().date():
            print(f"{person.name} was born before current date. BirthDate: {birth_date}, Current date: {current_time}")
            verify = False
        if person.death != 'N/A':
            death = datetime.strptime(datetime.strptime(person.death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if death > current_time:
                print(f"{person.name} was died before current date. Death: {person.death}, Current date: {current_time}")
                verify = False
    for family_member in Project.familyList:
        if family_member.married != 'N/A':
            marry_date = datetime.strptime(datetime.strptime(family_member.married, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if marry_date > current_time:
                print(f"{family_member.husbandName} and {family_member.wifeName} married before current date. Married: {marry_date}, Current Date: {current_time}")
        if family_member.divorce != 'NA':
            divorce_date = datetime.strptime(datetime.strptime(family_member.divorce, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            if divorce_date > current_time:
                print(f"{family_member.husbandName} and {family_member.wifeName} divorced before current date. Married: {divorce_date}, Current Date: {current_time}")
    if verify:
        print("All dates happen before current date.")
    else:
        print("Not all dates happen before current date.")


def main():
    """ run the code """
    Project.main()
    us01()


if __name__ == '__main__':
    main()

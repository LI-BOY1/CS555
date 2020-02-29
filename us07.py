import Project
from datetime import datetime

def us07():
    # Less then 150 years old
    """
    Death less than 150 years after birth for dead people
    current date less than 150 years after birth for all living people
    """
    flag = True
    date_now = datetime.now().date()
    for person in Project.personList:
        #check dead people
        if person.alive == False:
            # get death
            death_date = datetime.strptime(datetime.strptime(person.death,'%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            # get birth
            birth_date = datetime.strptime(datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            div_time = (death_date - birth_date).days/365.25
            if div_time > 150:
                print(f"ERROR: INDIVIDUAL: US07: {person.id}: more than 150 years old")
                flag = False
        else:
            # get birth
            birth_date = datetime.strptime(datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
            div_time = (date_now - birth_date).days/365.25
            if div_time > 150:
                print(f"ERROR: INDIVIDUAL: US07: {person.id}: more than 150 years old")
                flag = False

    if flag:
        return 'Correct'
    else:
        return 'Error'


def main():
    Project.main()
    print(us07())

if __name__ == "__main__":
    main()
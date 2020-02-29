import Project
from datetime import datetime

def us08():
    # Birth before marriage of parents
    """
    Children should be born after marriage of parents 
    (and not more than 9 months after their divorce)
    """

    flag = True
    for person in Project.personList:
        key = person.child
        ky = "".join(key)
        birth_date = datetime.strptime(datetime.strptime(person.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
        for i in range(len(Project.familyList)):
            if Project.familyList[i].id == ky:
                married_date = datetime.strptime(datetime.strptime(Project.familyList[i].married, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                if married_date > birth_date:
                    print(f"ERROR: INDIVIDUAL: US07: {person.id}: both before marriage")
                    flag = False
                    
                divorce = Project.familyList[i].divorce
                if divorce != 'NA':
                    divorce_date = datetime.strptime(datetime.strptime(Project.familyList[i].divorce, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                    dif_time = ((birth_date - divorce_date).days/365.25) * 12
                    # print(dif_time)
                    if dif_time > 9:
                        print(f"ERROR: INDIVIDUAL: US07: {person.id}: both before marriage")
                        flag = False
    if flag:
        return "Correct"
    else:
        return "Error"

def main():
    Project.main()
    print(us08())

if __name__ == "__main__":
    main()


import Project
from datetime import datetime

def us09():
    # Birth before death of parents
    """
    Child should be born before death of mother
    and before 9 months after death of father
    """

    flag = True
    for i in Project.familyList:
        child_key = i.id
        hus_key = i.husbandID
        wife_key = i.wifeID
        # print(child_key)

        for j in Project.personList:
            aa = "".join(j.child)
            # get child birth date
            if aa == child_key:
                birth_date = datetime.strptime(datetime.strptime(j.birthDate, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
                print(birth_date)
                for m in Project.familyList:
                    if 

    #         # # get father death date
    #         # if (Project.personList[j].id == hus_ky) and (Project.personList[j].death != 'N/A'):
    #         #     hus_death = datetime.strptime(datetime.strptime(Project.personList[j].death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()

    #         # else:
    #         #     hus_death = 'N/A'            

        # for m in Project.personList:
        #     # get mother death date
        #     if m.id == wife_key:
        #         # print(m.death)
        #         wife_death = datetime.strptime(datetime.strptime(m.death, '%d %b %Y').strftime("%Y-%m-%d"), '%Y-%m-%d').date()
        #         w_death = str(wife_death)
        #         print(w_death)
        #     else:
        #         print("NA")
            
    #         # check child with mom
    #             if wife_death != 'N/A' and wife_death < birth_date :
    #                 flag = False
    #                 print("Error: INDIVIDUAL: US09: " + str(j) + child_key + ": " + b_date + " before " + w_death)
            
    #         # check child with father


    # if flag:
    #     print("Correct!")

def main():
    Project.main()
    us09()

if __name__ == "__main__":
    main()

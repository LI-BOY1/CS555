def us10(personList, familyList):
    # Marriage after 14
    """Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)"""
    flag = True
    for person in personList:
        if person.spouse != "":
            if person.age < 14:
                res = "ERROR: INDIVIDUAL: US10: " + person.id + ": Marriage after 14"
                print(res)
                flag = False
    if flag:
        return "Correct"
    else:
        return "Error"

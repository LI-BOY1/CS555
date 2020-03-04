import datetime

def compare_date(date1, date2):
    """
    by qw
    """
    c_date1 = datetime.datetime.strptime(date1, '%d %b %Y').date() 
    c_date2 = datetime.datetime.strptime(date2, '%d %b %Y').date()
    if c_date1 > c_date2:
        return 1
    elif c_date1 < c_date2:
        return -1
    else:
        return 0


def US02(out_file, personList, familyList, print_flag=True):
    """
    by qw
    To check if there is any violation of "Birth should occur before marriage of an individual"
    out_file: the path of output file
    print_flag: boolean, whether the function output to a file or not 
    """
    error = 0
    for f in familyList:
        for p in personList:

            if p.id == f.wifeID:
                if compare_date(p.birthDate, f.married) == 1:
                    error += 1
                    if print_flag:
                        print("ERROR: FAMILY: US02: " + f.id + " Wife's birth date " + str(birth_date) + " following marriage date " + str(marry_date))

            if p.id == f.husbandID:
                if compare_date(p.birthDate, f.married) == 1:
                    error += 1
                    if print_flag:
                            print(error_msg = "ERROR: FAMILY: US02: " + f.id + " Husband's birth date " + str(birth_date) + " following marriage date " + str(marry_date))
                            
    return error   


def US03(personList, print_flag=True):
    """
    by qw
    To check if there is any violation of "Birth should occur before death of an individual"

    print_flag: boolean, whether the function output to a file or not 
    """
    error = 0
    for p in personList:
        if p.death == "N/A":
            continue
        
        death_date = datetime.datetime.strptime(p.death, '%d %b %Y').date()
        birth_date = datetime.datetime.strptime(p.birthDate, '%d %b %Y').date()
        if compare_date(p.birthDate, p.death) == 1:
            error += 1
            if print_flag:
                print("ERROR: INDIVIDUAL: US03: " + p.id + " Died " + str(death_date) + " before born " + str(birth_date))

    return error   

         
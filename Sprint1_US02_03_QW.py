import datetime


def US02(out_file, personList, familyList, write_file=True):
    """
    by qw
    To check if there is any violation of "Birth should occur before marriage of an individual"
    out_file: the path of output file
    write_file: boolean, whether the function output to a file or not 
    """
    error = 0
    for f in familyList:
        for p in personList:

            if p.id == f.wifeID:
                birth_date = datetime.datetime.strptime(p.birthDate, '%d %b %Y').date() 
                marry_date = datetime.datetime.strptime(f.married, '%d %b %Y').date()
                if birth_date > marry_date:
                    error += 1
                    if write_file:
                        with open(out_file, 'a') as file:
                            error_msg = "ERROR: FAMILY: US02: " + f.id + " Wife's birth date " + str(birth_date) + " following marriage date " + str(marry_date)
                            file.write(error_msg)
                            file.write('\n')

            if p.id == f.husbandID:
                birth_date = datetime.datetime.strptime(p.birthDate, '%d %b %Y').date() 
                marry_date = datetime.datetime.strptime(f.married, '%d %b %Y').date()
                if birth_date > marry_date:
                    error += 1
                    if write_file:
                        with open(out_file, 'a') as file:
                            error_msg = "ERROR: FAMILY: US02: " + f.id + " Husband's birth date " + str(birth_date) + " following marriage date " + str(marry_date)
                            file.write(error_msg)
                            file.write('\n')

    return error   


def US03(out_file, personList, write_file=True):
    """
    by qw
    To check if there is any violation of "Birth should occur before death of an individual"
    out_file: the path of output file
    write_file: boolean, whether the function output to a file or not 
    """
    error = 0
    for p in personList:
        if p.death == "N/A":
            continue
        
        death_date = datetime.datetime.strptime(p.death, '%d %b %Y').date()
        birth_date = datetime.datetime.strptime(p.birthDate, '%d %b %Y').date()
        if birth_date > death_date:
            error += 1
            if write_file:
                with open(out_file, 'a') as file:
                    error_msg = "ERROR: INDIVIDUAL: US03: " + p.id + " Died " + str(death_date) + " before born " + str(birth_date)
                    file.write(error_msg)
                    file.write('\n')
    return error   

         
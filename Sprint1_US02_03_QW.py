import datetime


def US02(out_file, personList, familyList):
    """
    by qw
    To check if there is any violation of "Birth should occur before marriage of an individual"
    """
    for f in familyList:
        for p in personList:

            if p.id == f.wifeID:
                birth_date = datetime.datetime.strptime(p.birthDate, '%d %b %Y').date() 
                marry_date = datetime.datetime.strptime(f.married, '%d %b %Y').date()
                if birth_date > marry_date:
                    with open(out_file, 'a') as file:
                        error_msg = "ERROR: FAMILY: US02: " + f.id + " Wife's birth date " + str(birth_date) + " following marriage date " + str(marry_date)
                        file.write(error_msg)
                        file.write('\n')

            if p.id == f.husbandID:
                birth_date = datetime.datetime.strptime(p.birthDate, '%d %b %Y').date() 
                marry_date = datetime.datetime.strptime(f.married, '%d %b %Y').date()
                if birth_date > marry_date:
                    with open(out_file, 'a') as file:
                        error_msg = "ERROR: FAMILY: US02: " + f.id + " Husband's birth date " + str(birth_date) + " following marriage date " + str(marry_date)
                        file.write(error_msg)
                        file.write('\n')             


def US03(out_file, personList):
    """
    by qw
    To check if there is any violation of "Birth should occur before death of an individual"
    """

    for p in personList:
        if p.death == "N/A":
            continue
        
        death_date = datetime.datetime.strptime(p.death, '%d %b %Y').date()
        birth_date = datetime.datetime.strptime(p.birthDate, '%d %b %Y').date()
        if birth_date > death_date:
            with open(out_file, 'a') as file:
                error_msg = "ERROR: INDIVIDUAL: US03: " + p.id + " Died " + str(death_date) + " before born " + str(birth_date)
                file.write(error_msg)
                file.write('\n')

         
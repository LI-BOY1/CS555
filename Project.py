def process_line(line):
    valid_tages = {
        '0': ('HEAD', 'NOTE', 'TRLR'),
        '1': ('BIRT', 'CHIL', 'DEAT', 'DIV', 'FAMC', 'FAMS', 'HUSB', 'MARR', 'NAME', 'SEX', 'WIFE'),
        '2': ('DATE')}

    # print(f"-->{line}")

    tokens = line.split()

    if len(tokens) == 3 and tokens[0] == '0' and tokens[2] in ('INDI', 'FAM'):
        level, args, tag = tokens
        valid = 'Y'
    elif len(tokens) >= 2:
        level, tag, args = tokens[0], tokens[1], " ".join(tokens[2:])
        valid = 'Y' if level in valid_tages and tag in valid_tages[level] else 'N'
    else:
        level, tag, valid, args = tokens, "NA", 'N', 'NA'

    print(f"<-- {level}|{tag}|{valid}|{args}")


def main():
    file = "/Users/boyli/Desktop/Boyang Li.ged"

    try:
        fp = open(file);
    except FileNotFoundError:
        print("Can't open your ", file)
    else:
        with fp:
            for line in fp:
                process_line(line.strip())



if __name__ == '__main__':
    main()

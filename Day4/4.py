def load_data(input_file):
    with open(input_file) as puzzle:
        return [x.strip() for x in puzzle.readlines()]


def validate_field(key, value):
    if key == 'byr':
        if int(value) >= 1920 and int(value) <= 2002:
            return True

    if key == 'iyr':
        if int(value) >= 2010 and int(value) <= 2020:
            return True

    if key == 'eyr':
        if int(value) >= 2020 and int(value) <= 2030:
            return True

    if key == 'hgt':
        if 'cm' in value:
            if 150 <= int(value[:-2]) <= 193:
                return True
        if 'in' in value:
            if 59 <= int(value[:-2]) <= 76:
                return True

    if key == 'hcl':
        if value[0] == '#' and len(value[1:]) == 6:
            return True

    if key == 'ecl':
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value in colors:
            return True


    if key == 'pid':
        if len(value) == 9:
            count = 0
            for char in value:
                if char.isdigit():
                    count += 1
            if count == 9:
                return True


def check_passports(input_file):
    data = load_data(input_file)
    print(data)
    ok_passport_count = 0
    req = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    current = 0
    tot_passports = 0
    for line in data:
        for field in line.split():
            key, val = field.split(":")
            #if key in req:    # <-- Case 1
            if validate_field(key, val) == True:   # <-- Case 2
                current += 1
        if line == "" or line == data[-1]:
            tot_passports +=1
            if current == len(req):
                ok_passport_count += 1
            current = 0

    print("Total passports: {}".format(tot_passports))
    print("Total ok passports: {}, {}% of total".format(
        ok_passport_count, round((ok_passport_count/tot_passports)*100))
    )
    return ok_passport_count


print(check_passports("input.txt"))

# 218 (low)
# 219 (correct!)
# 286 (high)
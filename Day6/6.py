
def load_data(puzzle_file):
    with open(puzzle_file) as file:
        return [x.strip() for x in file.readlines()]


def make_groups():
    persons = load_data('input.txt')
    group_temp = []
    groups = []

    for person in persons:
        if person == persons[-1]:
            group_temp.append(person)
            groups.append(group_temp)
        elif person != '':
            group_temp.append(person)
        elif person == '':
            groups.append(group_temp)
            group_temp = []
        else:
            raise Exception('something was fucked')
    return groups


def case_one():
    groups = make_groups()
    sum_yes_questions = 0
    for group in groups:
        yes_questions = []
        for guy in group:
            for answers in guy:
                if answers not in yes_questions:
                    yes_questions.append(answers)

        for _ in yes_questions:
            sum_yes_questions += 1
    print(sum_yes_questions)


def case_two():
    groups = make_groups()
    tot_counter = 0
    for group in groups:
        common_yeses = ''
        for guy in group:
            common_yeses += guy
        count = {}
        for s in common_yeses:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        for key in count:
            if count[key] >= len(group):
                tot_counter += 1
    print(tot_counter)


case_one()
case_two()

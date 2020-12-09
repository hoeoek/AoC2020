
def load_data():
    with open('input.txt') as file:
        return [x.strip() for x in file.readlines()]


def generate_list():
    list_of_rules = load_data()
    bag_rules = []
    for rule in list_of_rules:

        rule = rule.split('contain ')
        bag_type = rule[0]
        bags_contained = rule[1].split(', ')
        # print(bag_type, bags_contained)
        bag_rules.append([bag_type, bags_contained])

    return bag_rules


def finder(bag_color):
    bag_rules = generate_list()
    res = []
    for rule in bag_rules:
        if bag_color in rule[0]:
            # print(rule)
            res.append(rule[1])
    return res[0]


def looper(start):
    bag_steps = 0
    bag_list = []
    first = finder(start)
    bag_list.append(first)
    res = []

    for bags in bag_list:
        for bag in bags:
            if 'no other' in bag:
                pass


            else:
                #print('looking at bag {}'.format(bag))
                search_word_color = bag[2:-5]
                bag_list.append(finder(search_word_color))
                print(search_word_color)
                res.append(search_word_color)
    print(res)
    print(len(res))
    print(set(res))
    print(len(set(res)))




looper('shiny gold')


# Guesses
# 31
# 30

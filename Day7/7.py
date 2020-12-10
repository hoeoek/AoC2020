
def load_data():
    with open('input.txt') as file:
        return [x.strip() for x in file.readlines()]


rules = load_data()

# The following two paragraphs are cheated, but i was trying to do this basically

bags = {}
for rule in rules:
    bag, contains = rule.split('contain')
    bag = bag.replace(' bags', '')
    bags[bag] = contains


answer = set()
q = ['shiny gold']
while len(q) != 0:
    current = q.pop(0)
    for bag in bags:
        if bag in answer:
            continue
        if current in bags[bag]:
            q.append(bag)
            answer.add(bag)
    print(q)
print(answer)
print(len(answer))







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


def case_one(start):
    bag_list = finder(start)
    bag_list = bag_list_to_colors(bag_list)
    print(bag_list)
    for bag in bag_list:
        print(bag)

        print(bag_list_to_colors(finder(bag)))
        bag_list.append(bag_list_to_colors(finder(bag)))




def bag_list_to_colors(bag_list):
    res = []
    for bag in bag_list:
        if 'no other' in bag:
            break
        else:
            bag = bag.split(' ')
            res.append(bag[1] + ' ' + bag[2])
    return res



# Guesses
# 31
# 30
# 27

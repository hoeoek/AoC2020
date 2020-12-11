
import csv

puzzle = "input.txt"
def slope_counter(right, down):
    with open(puzzle) as file:
        reader = csv.reader(file)
        small_map = []
        for line in reader:
            small_map.append(line)

    detailed_map = small_map
    for i, line in enumerate(small_map):
        detailed_map[i] = ([char for char in line[0]])

    x, y = 0, 0
    tree_count = 0
    for line in detailed_map:
        y += down
        x += right

        if y > len(detailed_map)-1:
            break

        if x > len(line)-1:
            x = x % len(line)

        if detailed_map[y][x] == "#":
            tree_count += 1
            detailed_map[y][x] = "X"
        else:
            detailed_map[y][x] = "O"



    print("Tree count: {}".format(tree_count))
    return tree_count

q=slope_counter(1,1)
w=slope_counter(3,1)
e=slope_counter(5,1)
r=slope_counter(7,1)
t=slope_counter(1,2)

print("total: {}".format(q*w*e*r*t))


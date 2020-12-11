def load_data(file):
    with open(file) as f:
        return [x.strip() for x in f.readlines()]


def build_plane():
    plane = []
    for i in range(0, 127):
        plane.append(['O' for x in range(0, 8)])
    return plane


def populate_plane(plane, seat_list):
    for ticket in seat_list:
        plane[ticket[0]][ticket[1]] = 'X'
    return plane


def step_feeder(boarding_pass):
    row_chars = boarding_pass[:7]
    col_chars = boarding_pass[-3:]
    #print('{}, {}, {}'.format(row_chars, col_chars, boarding_pass))
    included = [0, 127]
    result = []
    for i, row_char in enumerate(row_chars):
        #print(i, row_char)
        low = included[0]
        high = included[1]
        half_diff = int((high-low)/2)
        if row_char == 'F':
            included = [low, high-1-half_diff]
            #print(included)
        elif row_char == 'B':
            included = [low+1+half_diff, high]
            #print(included)
        else:
            print('something fucked up 1')
    if included[0] == included[1]:
        result = ['placeholder', included[0]]
    included = [0, 7]
    for i, col_char in enumerate(col_chars):
        left = included[0]
        right = included[1]
        half_diff = int((right-left)/2)
        if col_char == 'L':
            included = [left, right-1-half_diff]
        elif col_char == 'R':
            included = [left+1+half_diff, right]
    if included[0] == included[1]:
        result[0] = included[0]
    seat_id = result[1] * 8 + result[0]
    return [seat_id, [result[1], result[0]]]


step_feeder('FBFBBFFRLR')
boardingpasses = load_data('input.txt')

seat_ids = []
plane = build_plane()
for boardingpass in boardingpasses:
    seat_ids.append(step_feeder(boardingpass))
    coord = step_feeder(boardingpass)[1]
    #print(coord)
    #print(plane[coord[0]])
    plane[coord[0]][coord[1]] = 'X'
    #print(plane[coord[0]])
for i, row in enumerate(plane):
    print(i, row)
for line in plane:
    print("".join(line))

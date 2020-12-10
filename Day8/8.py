def load_data():
    with open('input.txt') as file:
        reader = file.readlines()
        instructions = {}
        for i, line in enumerate(reader):
            line = line.strip()
            instructions[i] = line.split(' ')
    return instructions


load_data()
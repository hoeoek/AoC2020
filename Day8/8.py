def load_data():
    with open('input.txt') as file:
        reader = file.readlines()
        instructions = {}
        for i, line in enumerate(reader):
            line = line.strip()
            instructions[i] = line.split(' ')
    return instructions


instructions = load_data()


running = True
current_step = 0
accumulator = 0
visited = []

while running:
    if current_step in visited:
        print(accumulator)
        running = False
    visited.append(current_step)
    if instructions[current_step][0] == 'acc':
        accumulator += int(instructions[current_step][1])
        current_step += 1
    if instructions[current_step][0] == 'jmp':
        current_step += int(instructions[current_step][1])
    if instructions[current_step][0] == 'nop':
        current_step += 1
def load_data():
    with open('input.txt') as file:
        reader = file.readlines()
        instructions = {}
        for i, line in enumerate(reader):
            line = line.strip()
            instructions[i] = line.split(' ')
    return instructions


def case_one():
    instructions = load_data()
    current_step = 0
    accumulator = 0
    visited = []
    while True:
        if current_step in visited:
            return accumulator
        visited.append(current_step)
        if instructions[current_step][0] == 'acc':
            accumulator += int(instructions[current_step][1])
            current_step += 1
        if instructions[current_step][0] == 'jmp':
            current_step += int(instructions[current_step][1])
        if instructions[current_step][0] == 'nop':
            current_step += 1


def check_if_not_loop(mod_instruction):
    instructions = mod_instruction
    current_step = 0
    accumulator = 0
    visited = []

    while True:
        if current_step == len(instructions):
            print('Program didnt loop!')
            return accumulator
        if current_step in visited:
            print('Program looped at step {}'.format(current_step))
            return accumulator
        visited.append(current_step)
        if instructions[current_step][0] == 'acc':
            accumulator += int(instructions[current_step][1])
            current_step += 1
        if instructions[current_step][0] == 'jmp':
            current_step += int(instructions[current_step][1])
        if instructions[current_step][0] == 'nop':
            current_step += 1

instructions = load_data()

check_if_not_loop(instructions)


def batch_of_instructions():
    batch = []
    pass

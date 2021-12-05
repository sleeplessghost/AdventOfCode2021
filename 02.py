instructions = [line.strip().split(' ') for line in open('in/02.txt')]
parsedInstructions = [(direction, int(value)) for [direction, value] in instructions]

x, y = 0, 0
for instr in parsedInstructions:
    match instr:
        case ['up', value]: y -= value
        case ['down', value]: y += value
        case ['forward', value]: x += value
print('part1:', x * y)

x, y, aim = 0, 0, 0
for instr in parsedInstructions:
    match instr:
        case ['up', value]: aim -= value
        case ['down', value]: aim += value
        case ['forward', value]: x += value; y += value * aim
print('part2:', x * y)
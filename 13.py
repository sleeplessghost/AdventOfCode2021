def fold(dots, instruction):
    axis, value = instruction.split('=')
    value = int(value)
    return {foldPoint(point, axis, value) for point in dots}

def foldPoint(point, axis, value):
    x,y = point
    if axis == 'x' and x > value: x = value + value - x
    if axis == 'y' and y > value: y = value + value - y
    return (x,y)

def printDots(dots):
    rx, ry = max(x for x,y in dots), max(y for x,y in dots)
    text = [['  ' for _ in range(rx + 1)] for _ in range(ry + 1)]
    for x,y in dots: text[y][x] = '██'
    for line in text: print(''.join(line))

dots, instructions = open('in/13.txt').read().split('\n\n')
dots = {tuple(int(p) for p in line.split(',')) for line in dots.split()}
instructions = [i.strip().replace("fold along ", "") for i in instructions.split('\n')]

print('part1:', len(fold(dots, instructions[0])))

for instr in instructions: dots = fold(dots, instr)
print('part2:')
printDots(dots)
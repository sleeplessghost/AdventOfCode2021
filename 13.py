from collections import defaultdict

def foldgrid(grid, instruction):
    axis, value = instruction.split('=')
    value = int(value)
    maxy = max(y for x,y in grid) + 1
    maxx = max(x for x,y in grid) + 1
    if axis == 'x':
        for x in range(value, maxx):
            diff = x - value
            mirrorX = x - diff - diff
            for y in range(maxy):
                if (x,y) in grid:
                    if grid[(x,y)]:
                        grid[(mirrorX,y)] = True
                    del grid[(x,y)]
    elif axis == 'y':
        for y in range(value, maxy):
            diff = y - value
            mirrorY = y - diff - diff
            for x in range(maxx):
                if (x,y) in grid:
                    if grid[(x,y)]:
                        grid[(x,mirrorY)] = True
                    del grid[(x,y)]

def printGr(grid):
    for y in range(max(y for x,y in grid) + 1):
        for x in range(max(x for x,y in grid) + 1):
            if grid[(x,y)]: print('X', end="")
            else: print(" ", end="")
        print()

dots, instructions = open('in/13.txt').read().split('\n\n')
dots = [x.strip().split(',') for x in dots.split()]
instructions = [x.strip().replace("fold along ", "") for x in instructions.split('\n')]

grid = defaultdict(bool)
for x,y in dots:
    grid[(int(x), int(y))] = True

p1 = grid.copy()
foldgrid(p1, instructions[0])
print('part1', sum(v for v in p1.values()))

p2 = grid.copy()
for instr in instructions:
    foldgrid(p2, instr)

printGr(p2)
print('part2:', 'read above')
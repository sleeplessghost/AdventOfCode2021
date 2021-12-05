from collections import defaultdict

def parseLine(line):
    return [list(map(int, p.split(','))) for p in line.split(' -> ')]

def isStraight(line):
    [[x1,y1], [x2,y2]] = line
    return x1 == x2 or y1 == y2

def drawLines(grid, lines):
    for line in lines:
        [[x1,y1], [x2,y2]] = line
        if x1 == x2:
            for y in range(min(y1,y2), max(y1,y2) + 1):
                grid[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1,x2), max(x1,x2) + 1):
                grid[(x, y1)] += 1
        else:
            stepX = 1 if x2 > x1 else -1
            stepY = 1 if y2 > y1 else -1
            for x,y in zip(range(x1, x2 + stepX, stepX), range(y1, y2 + stepY, stepY)):
                grid[(x,y)] += 1
    return grid

lines = [parseLine(x.strip()) for x in open('in/05.txt')]
straights = [l for l in lines if isStraight(l)]
diagonals = [l for l in lines if not isStraight(l)]
grid = defaultdict(int)

drawLines(grid, straights)
print('part1:', sum(v > 1 for v in grid.values()))

drawLines(grid, diagonals)
print('part2:', sum(v > 1 for v in grid.values()))


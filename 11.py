from itertools import product
def octomap(input):
    return {(x,y): int(input[y][x]) for x in range(len(input[0])) for y in range(len(input))}

def neighbours(octos, x, y):
    points = [(x+dx, y+dy) for dx in range(-1,2) for dy in range(-1,2) if dx or dy]
    return [p for p in points if p in octos]

def countFlashes(octos, steps):
    flashes = 0
    for _ in range(steps):
        for point in octos: octos[point] += 1
        while (flashpts:= [p for p in octos if octos[p] > 9]):
            for point in flashpts:
                octos[point] = -999999999999
                for n in neighbours(octos, *point): octos[n] += 1
        flashes += len(flashed:= [p for p in octos if octos[p] < 0])
        for point in flashed: octos[point] = 0
    return flashes

def synchronize(octos):
    step = 0
    while not all(v == 0 for v in octos.values()):
        step += 1
        countFlashes(octos, 1)
    return step

octos = octomap([line.strip() for line in open('in/11.txt')])
print('part1:', countFlashes(octos.copy(), 100))
print('part2:', synchronize(octos.copy()))
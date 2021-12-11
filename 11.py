def octomap(input):
    return {(x,y): int(input[y][x]) for x in range(len(input[0])) for y in range(len(input))}

def neighbours(x, y):
    return [(x-1,y), (x+1,y), (x,y-1), (x,y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]

def countFlashes(octos, steps):
    flashes = 0
    for _ in range(steps):
        for point in octos: octos[point] += 1
        flashpts = [p for p in octos if octos[p] > 9]
        while len(flashpts):
            for point in flashpts:
                octos[point] = -999999999999
                for p in neighbours(*point):
                    if p in octos: octos[p] += 1
            flashpts = [p for p in octos if octos[p] > 9]
        flashpts = [p for p in octos if octos[p] < 0]
        flashes += len(flashpts)
        for p in flashpts: octos[p] = 0
    return flashes

def synchronize(octos):
    step = 0
    while not all(octos[p] == 0 for p in octos):
        step += 1
        countFlashes(octos, 1)
    return step

octos = octomap([line.strip() for line in open('in/11.txt')])
print('part1:', countFlashes(octos, 100))

octos = octomap([line.strip() for line in open('in/11.txt')])
print('part2:', synchronize(octos))
def parseCaves(lines):
    caves = {}
    for line in lines:
        a,b = line.split('-')
        if a not in caves:
            caves[a] = [b]
        else: caves[a].append(b)
        if b not in caves:
            caves[b] = [a]
        else: caves[b].append(a)
    return caves

def isSmall(cave): return cave.islower()

def getPaths(caves):
    return [path for path in search(caves, ['start'])]

def getPaths2(caves):
    return [path for path in search2(caves, ['start'])]

def search(caves, path):
    current = path[-1]
    if current == 'end': yield [*path, current]
    else:
        connected = caves[current]
        for c in connected:
            if c != 'start':
                if not isSmall(c) or c not in path: yield from search(caves, [*path, c])

def search2(caves, path):
    current = path[-1]
    if current == 'end': yield [*path, current]
    else:
        connected = caves[current]
        for c in connected:
            if c != 'start':
                if not isSmall(c) or c not in path: yield from search2(caves, [*path, c])
                else:
                    smalls = {cave: path.count(cave) for cave in path if isSmall(cave)}
                    if not any(v >= 2 for v in smalls.values()): yield from search2(caves, [*path, c])

caves = parseCaves([x.strip() for x in open('in/12.txt')])

print('part1:', len(getPaths(caves)))
print('part2:', len(getPaths2(caves)))
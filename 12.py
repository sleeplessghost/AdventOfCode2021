from collections import defaultdict

def parseCaves(lines):
    caves = defaultdict(set)
    for a,b in [line.split('-') for line in lines]:
        caves[a].add(b)
        caves[b].add(a)
    return caves

def isSmall(cave): return cave.islower()

def getPaths(caves, doubleSmall):
    return [path for path in search(caves, ['start'], doubleSmall)]

def search(caves, path, doubleSmall):
    current = path[-1]
    if current == 'end': yield path
    else:
        connected = [c for c in caves[current] if c != 'start']
        for c in connected:
            if not isSmall(c) or c not in path:
                yield from search(caves, [*path, c], doubleSmall)
            elif doubleSmall and not any(path.count(cave) >= 2 for cave in path if isSmall(cave)):
                yield from search(caves, [*path, c], doubleSmall)

caves = parseCaves([x.strip() for x in open('in/12.txt')])
print('part1:', len(getPaths(caves, False)))
print('part2:', len(getPaths(caves, True)))
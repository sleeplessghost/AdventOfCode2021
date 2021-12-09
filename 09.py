from collections import deque
from math import prod

def heightmap(input):
    return {(x,y): int(input[y][x]) for x in range(len(input[0])) for y in range(len(input))}

def neighbours(x, y):
    return [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

def findLows(mapped):
    return [point for point in mapped if isLow(mapped, point)]

def isLow(mapped, point):
    return all(n not in mapped or mapped[n] > mapped[point] for n in neighbours(*point))

def isTraversable(mapped, start, end):
    return end in mapped and mapped[end] > mapped[start] and mapped[end] < 9

def basinSize(mapped, low):
    basin, queue = set(), deque([low])
    while(queue):
        point = queue.popleft()
        basin.add(point)
        points = [n for n in neighbours(*point) if isTraversable(mapped, point, n)]
        for p in points: queue.append(p)
    return len(basin)

mapped = heightmap([line.strip() for line in open('in/09.txt')])
lows = findLows(mapped)
basins = [basinSize(mapped, low) for low in lows]
basins.sort()

print('part1:', sum(mapped[point] + 1 for point in lows))
print('part2:', prod(basins[-3:]))



from heapq import heappop, heappush
from collections import defaultdict
import numpy as np

def neighbours(x, y):
    return [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

def getMap(inputs):
    return {(x,y): inputs[y][x] for x in range(len(inputs[0])) for y in range(len(inputs))}

def lowestRisk(mapped):
    target = max(mapped)
    q, visited = [(0, (0,0))], defaultdict(bool)
    visited[(0,0)] = True
    while q:
        risk, point = heappop(q)
        if point == target: return risk
        nextPoints = [n for n in neighbours(*point) if n in mapped and not visited[n]]
        for n in nextPoints:
            visited[n] = True
            heappush(q, (risk + mapped[n], n))

def makeBigger(inputs):
    LX, LY = len(inputs[0]), len(inputs)
    tiled = np.tile(inputs, (5, 5))
    return [[(tiled[y][x] + x//LX + y//LY -1) % 9 + 1 for x in range(5 * LX)] for y in range(5 * LY)]

input = [[int(n) for n in x.strip()] for x in open('in/15.txt')]
bigInput = makeBigger(input)

mapped = getMap(input)
print('part1:', lowestRisk(mapped))
mapped = getMap(bigInput)
print('part2:', lowestRisk(mapped))
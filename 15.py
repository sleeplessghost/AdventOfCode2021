from heapq import heappop, heappush
import numpy as np

def neighbours(x, y):
    return [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

def getRisks(mapped):
    risks, q = {}, []
    heappush(q, (0, (0,0)))
    while q:
        risk, point = heappop(q)
        if risk not in risks or risk < risks[point]:
            risks[point] = risk
            nextPoints = [n for n in neighbours(*point) if n in mapped]
            for n in nextPoints:
                r = risk + mapped[n]
                if n not in risks or r < risks[n]:
                    risks[n] = r
                    heappush(q, (r, n))
    return risks

def makeBigger(inputs):
    LX, LY = len(inputs[0]), len(inputs)
    tiled = np.tile(inputs, (5, 5))
    for y in range(5 * LY):
        for x in range(5 * LX):
            if x >= LX or y >= LY:
                tiled[y][x] += (x // LX) + (y // LY)
                if tiled[y][x] > 9: tiled[y][x] %= 9
    return tiled

def getMap(inputs):
    return {(x,y): inputs[y][x] for x in range(len(inputs[0])) for y in range(len(inputs))}

def solve(input):
    mapped = getMap(input)
    risks = getRisks(mapped)
    return risks[(max(x for x,y in mapped), max(y for x,y in mapped))]

input = [[int(n) for n in x.strip()] for x in open('in/15.txt')]
bigInput = makeBigger(input)
print('part1:', solve(input))
print('part2:', solve(bigInput))
def neighbours(x, y):
    return [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

def riskmap(mapped):
    mx, my = max(x for x,y in mapped), max(y for x,y in mapped)
    risks = {(0,0): 0}
    for _ in range(3):
        for y in range(my + 1):
            for x in range(mx + 1):
                point = (x,y)
                riskToHere = risks[point]
                nextPoints = [n for n in neighbours(*point) if n in mapped]
                for n in nextPoints:
                    risk = riskToHere + mapped[n]
                    if n not in risks or risk < risks[n]: risks[n] = risk
    return risks

def quintmap(mapped):
    newmap = {}
    lx = max(x for x,y in mapped) + 1
    ly = max(y for x,y in mapped) + 1
    for (x,y), value in mapped.items():
        for mult in range(5):
            value = mapped[(x,y)] + (mult * 1)
            if value > 9: value = value % 9
            newmap[(x + (lx * mult), y)] = value
    secondmap = {}
    for (x,y), value in newmap.items():
        for mult in range(5):
            value = newmap[(x,y)] + (mult * 1)
            if value > 9: value = value % 9
            secondmap[(x, y + (ly * mult))] = value
    return secondmap

inputs = [[int(n) for n in x.strip()] for x in open('in/15.txt')]
mapped = {}
for y in range(len(inputs)):
    for x in range(len(inputs[0])):
        mapped[(x,y)] = inputs[y][x]

risks = riskmap(mapped)
print('part1:', risks[(max(x for x,y in mapped), max(y for x,y in mapped))])

bigger = quintmap(mapped)
risks = riskmap(bigger)
print('part2:', risks[(max(x for x,y in bigger), max(y for x,y in bigger))])
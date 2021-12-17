import re

def brute(xmin, xmax, ymin, ymax):
    bests = (bestY((x,y), xmin, xmax, ymin, ymax) for y in range(-1000, 1000) for x in range(1000))
    bests = [y for y in bests if y != None]
    return max(bests), len(bests)

def bestY(velocity, xmin, xmax, ymin, ymax):
    XV,YV = velocity
    xpos, ypos = 0,0
    besty = 0
    while xpos <= xmax and ypos >= ymin:
        xpos += XV
        ypos += YV
        if ypos > besty: besty = ypos
        if xmin <= xpos <= xmax and ymin <= ypos <= ymax:
            return besty
        if XV > 0: XV -= 1
        elif XV < 0: XV += 1
        YV -= 1
    return None

input = open('in/17.txt').readline()
xmin, xmax, ymin, ymax = [int(n) for n in re.search('.+x=(-?\d+)..(-?\d+).+y=(-?\d+)..(-?\d+)', input).groups()]
besty, count = brute(xmin, xmax, ymin, ymax)
print('part1:', besty)
print('part2:', count)
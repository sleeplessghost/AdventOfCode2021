from collections import deque
from math import floor

def corruptScore(line):
    q = deque()
    for c in line:
        if c in ['(', '[', '{', '<']: q.append(c)
        else:
            current = q.pop()
            if c != closingTag(current): return corruptVal(c)
    return 0

def completeLine(line):
    q = deque()
    for c in line:
        if c in ['(', '[', '{', '<']: q.append(c)
        else: q.pop()
    score = 0
    while(q): score = score * 5 + closingVal(closingTag(q.pop()))
    return score

def closingTag(c):
    match c:
        case '[': return ']'
        case '(': return ')'
        case '{': return '}'
        case '<': return '>'

def corruptVal(c):
    match c:
        case ')': return 3
        case ']': return 57
        case '}': return 1197
        case '>': return 25137

def closingVal(c):
    match c:
        case ')': return 1
        case ']': return 2
        case '}': return 3
        case '>': return 4

lines = [x.strip() for x in open('in/10.txt')]
corruptScores = [corruptScore(x) for x in lines]
incomplete = [x for x in lines if corruptScore(x) == 0]
incompleteScores = [completeLine(x) for x in incomplete]
incompleteScores.sort()

print('part1:', sum(corruptScores))
print('part2:', incompleteScores[floor(len(incompleteScores) / 2)])
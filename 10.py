from collections import deque, namedtuple
from functools import reduce

closingTags = { '(':')', '[':']', '{':'}', '<':'>' }
corruptValues = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
closingValues = { ')': 1, ']': 2, '}': 3, '>': 4 }
score = namedtuple('score', ['completion', 'corrupt'])

def lineScore(line):
    q = deque()
    for c in line:
        if c in ['(', '[', '{', '<']: q.append(c)
        elif c != closingTags[q.pop()]: return score(0, corruptValues[c])
    return score(completionScore(q), 0)

def completionScore(queue):
    queue.reverse()
    return reduce(lambda currentScore, c: currentScore * 5 + closingValues[closingTags[c]], queue, 0)

lines = [x.strip() for x in open('in/10.txt')]
scores = [lineScore(x) for x in lines]
completionScores = [s.completion for s in scores if s.completion > 0]
completionScores.sort()

print('part1:', sum(s.corrupt for s in scores))
print('part2:', completionScores[len(completionScores) // 2])
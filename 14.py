from collections import defaultdict

def pairDict(template):
    pairs = [''.join(x) for x in zip(template, template[1:])]
    return {p: pairs.count(p) for p in pairs}

def step(pairCounts, rules):
    after = defaultdict(int)
    for pair,count in pairCounts.items():
        if pair in rules:
            newPairs = (pair[0] + rules[pair], rules[pair] + pair[1])
            for p in newPairs: after[p] += count
        else: after[pair] += count
    return after

def countLetters(template, pairCounts):
    letterCounts = defaultdict(int)
    letterCounts[template[0]] += 1
    for pair,count in pairCounts.items(): letterCounts[pair[1]] += count
    return letterCounts

def solve(template, rules, iterations):
    temp = pairDict(template)
    for _ in range(iterations): temp = step(temp, rules)
    counts = countLetters(template, temp)
    return max(counts.values()) - min(counts.values())

template, rules = open('in/14.txt').read().split('\n\n')
rules = [line.split(' -> ') for line in rules.split('\n')]
rules = {pair: insertion for pair,insertion in rules}
print('part1:', solve(template, rules, 10))
print('part2:', solve(template, rules, 40))
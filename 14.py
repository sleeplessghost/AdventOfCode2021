from collections import defaultdict

def step(current, rules):
    pairs = [''.join(x) for x in zip(current, current[1:])]
    return pairs[0][0] + ''.join(getReplacement(pair, rules) for pair in pairs)

def getReplacement(pair, rules):
    if pair in rules:
        return rules[pair] + pair[1]
    return pair[1]

template, rules = open('in/14.txt').read().split('\n\n')
rules = [line.split(' -> ') for line in rules.split('\n')]
rules = {a: b for a,b in rules}

temp = template
for _ in range(10):
    temp = step(temp, rules)

counts = [temp.count(c) for c in set(temp)]
counts.sort()

print('part1:', counts[-1] - counts[0])

pairCounts = defaultdict(int)
pairs = [''.join(x) for x in zip(template, template[1:])]
for pair in pairs: pairCounts[pair] += 1

for i in range(40):
    temp = defaultdict(int)
    for pair in [p for p in pairCounts]:
        if pairCounts[pair] > 0:
            if pair in rules:
                results = (pair[0] + rules[pair], rules[pair] + pair[1])
                for p in results: temp[p] += pairCounts[pair]
            else: temp[pair] += pairCounts[pair]
    pairCounts = temp.copy()

letterCounts = defaultdict(int)
letterCounts[template[0]] += 1
for pair in pairCounts:
    a, b = pair
    letterCounts[b] += pairCounts[pair]
least = min(letterCounts.values())
most = max(letterCounts.values())
print('part2:', most - least)





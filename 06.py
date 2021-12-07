def countAfterDays(fish, days):
    counters = [sum(n == i for n in fish) for i in range(9)]
    for _ in range(days):
        counters.append(counters.pop(0))
        counters[6] += counters[8]
    return sum(counters)

fish = [int(n) for n in open('in/06.txt').read().split(',')]
print('part1:', countAfterDays(fish, 80))
print('part2:', countAfterDays(fish, 256))
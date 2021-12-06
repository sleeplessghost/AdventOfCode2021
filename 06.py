def countAfterDays(fish, days):
    counters = [sum(n == i for n in fish) for i in range(9)]
    for _ in range(days):
        zeroes = counters[0]
        for i in range(len(counters) - 1):
            counters[i] = counters[i + 1]
        counters[6] += zeroes
        counters[8] = zeroes
    return sum(counters)

fish = [int(n) for n in open('in/06.txt').read().split(',')]

print('part1:', countAfterDays(fish, 80))
print('part2:', countAfterDays(fish, 256))
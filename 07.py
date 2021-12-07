from functools import cache

@cache
def sumToN(n):               return n * (n+1) // 2
def basicFuel(nums, pos):    return sum(abs(n - pos) for n in nums)
def advancedFuel(nums, pos): return sum(sumToN(abs(n - pos)) for n in nums)

def calcFuel(nums, fuelFunc):
    return min([fuelFunc(nums, pos) for pos in range(min(nums), max(nums) + 1)])

nums = [int(n) for n in open('in/07.txt').read().split(',')]
print('part1:', calcFuel(nums, basicFuel))
print('part2:', calcFuel(nums, advancedFuel))
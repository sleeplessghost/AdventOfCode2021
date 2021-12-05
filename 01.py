def countIncreasing(numbers, count):
    increasing = 0
    for i in range(0, len(numbers) - count):
        a = sum(numbers[i : i+count])
        b = sum(numbers[i+1 : i+1+count])
        if b > a: increasing += 1
    return increasing

def onelinerA(numbers, count):
    return len([i for i in range(len(numbers) - count) if numbers[i + count] > numbers[i]])

def onelinerB(numbers, count):
    return sum(b > a for (a,b) in zip(numbers, numbers[count:]))

numbers = [int(n) for n in open('in/01.txt')]
print("part1:", countIncreasing(numbers, 1), onelinerA(numbers, 1), onelinerB(numbers, 1))
print("part2:", countIncreasing(numbers, 3), onelinerA(numbers, 3), onelinerB(numbers, 3))
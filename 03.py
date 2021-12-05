def mostCommonDigit(binaryStrings, i):
    total = sum([int(binary[i]) for binary in binaryStrings])
    return '1' if total > len(binaryStrings) / 2 else '0'

def reduceToSingle(binaryStrings, mostCommon, i = 0):
    if (len(binaryStrings) == 1): return binToNum(binaryStrings[0])
    zeroes = [x for x in binaryStrings if x[i] == '0']
    ones = [x for x in binaryStrings if x[i] == '1']
    reduced = getCommonality(zeroes, ones, mostCommon)
    return reduceToSingle(reduced, mostCommon, i+1)

def getCommonality(zeroes, ones, mostCommon):
    if mostCommon: return ones if len(ones) >= len(zeroes) else zeroes
    else: return zeroes if len(zeroes) <= len(ones) else ones

def binToNum(binaryString):
    return int(binaryString, 2)

binaryStrings = [x.strip() for x in open('in/03.txt')]

gamma = ''.join([mostCommonDigit(binaryStrings, i) for i in range(len(binaryStrings[0]))])
epsilon = ''.join(['1' if digit == '0' else '0' for digit in gamma])
oxygen = reduceToSingle(binaryStrings, True)
carbon = reduceToSingle(binaryStrings, False)

print('part1', binToNum(gamma) * binToNum(epsilon))
print('part2:', oxygen * carbon)
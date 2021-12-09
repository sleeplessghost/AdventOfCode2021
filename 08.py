
def count1478(signals):
    return sum(len(x) in [2, 3, 4, 7] for x in signals)

def convertOutput(line):
    signals, outputs = [[set(p) for p in patterns.split()] for patterns in line.split(' | ')]
    signals = {len(s): s for s in signals}
    return int(''.join(matchSignals(signals, o) for o in outputs))

def matchSignals(signals: dict[int, set], output: set):
    match len(output), len(output & signals[2]), len(output & signals[4]):
        case 2,_,_: return '1'
        case 3,_,_: return '7'
        case 4,_,_: return '4'
        case 5,1,2: return '2'
        case 5,2,3: return '3'
        case 5,1,3: return '5'
        case 6,2,3: return '0'
        case 6,1,3: return '6'
        case 6,2,4: return '9'
        case 7,_,_: return '8'

inputs = [x.strip() for x in open('in/08.txt')]
outputs = [x.split(' | ')[1].split() for x in inputs]
print('part1:', sum(count1478(x) for x in outputs))
print('part2:', sum(convertOutput(x) for x in inputs))
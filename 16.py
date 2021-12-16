from math import prod

class Packet:
    def __init__(self, version, id, literal, subpackets):
        self.version, self.id, self.literal, self.subpackets = version, id, literal, subpackets

    def sumVersions(self):
        return self.version + sum(p.sumVersions() for p in self.subpackets)
    
    def getValue(self):
        subValues = (p.getValue() for p in self.subpackets)
        match self.id:
            case 0: return sum(subValues)
            case 1: return prod(subValues)
            case 2: return min(subValues)
            case 3: return max(subValues)
            case 4: return self.literal
            case 5: return self.subpackets[0].getValue() > self.subpackets[1].getValue()
            case 6: return self.subpackets[0].getValue() < self.subpackets[1].getValue()
            case 7: return self.subpackets[0].getValue() == self.subpackets[1].getValue()

def parsePacket(binary):
    version, binary = int(binary[:3], 2), binary[3:]
    id, binary = int(binary[:3], 2), binary[3:]
    if id == 4: #value packet
        chunks = [binary[i:i+5] for i in range(0, len(binary), 5)]
        endIndex = next(i for i,chunk in enumerate(chunks) if chunk[0] == '0')
        binary = ''.join(chunks[endIndex+1:])
        literal = int(''.join([chunk[1:] for chunk in chunks[:endIndex+1]]), 2)
        return Packet(version, id, literal, []), binary
    else: #operator packet
        length, binary, subpackets = binary[0], binary[1:], []
        if length == '0':
            totalLength, binary = int(binary[:15], 2), binary[15:]
            sub, binary = binary[:totalLength], binary[totalLength:]
            while sub:
                packet, sub = parsePacket(sub)
                subpackets.append(packet)
        else:
            numSubs, binary = int(binary[:11], 2), binary[11:]
            for _ in range(numSubs):
                packet, binary = parsePacket(binary)
                subpackets.append(packet)
        return Packet(version, id, 0, subpackets), binary

hexi = open('in/16.txt').read()
binary = ''.join([bin(int(c, 16))[2:].zfill(4) for c in hexi])
packet, _ = parsePacket(binary)
print('part1:', packet.sumVersions())
print('part2:', packet.getValue())
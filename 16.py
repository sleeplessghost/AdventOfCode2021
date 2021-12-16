from math import prod

class Packet:
    def __init__(self, version, id, value, subpackets):
        self.version = version
        self.id = id
        self.value = value
        self.subpackets = subpackets

    def sumVersions(self):
        return self.version + sum(p.sumVersions() for p in self.subpackets)
    
    def getValue(self):
        subValues = [p.getValue() for p in self.subpackets]
        match self.id:
            case 0: return sum(subValues)
            case 1: return prod(subValues)
            case 2: return min(subValues)
            case 3: return max(subValues)
            case 4: return self.value
            case 5: return 1 if self.subpackets[0].getValue() > self.subpackets[1].getValue() else 0
            case 6: return 1 if self.subpackets[0].getValue() < self.subpackets[1].getValue() else 0
            case 7: return 1 if self.subpackets[0].getValue() == self.subpackets[1].getValue() else 0

    @staticmethod
    def parsePacket(binary):
        version, binary = int(binary[:3], 2), binary[3:]
        id, binary = int(binary[:3], 2), binary[3:]
        if id == 4: #value packet
            chunks = [binary[i:i+5] for i in range(0, len(binary), 5)]
            endIndex = next(i for i,chunk in enumerate(chunks) if chunk[0] == '0')
            binary = ''.join(chunks[endIndex+1:])
            value = int(''.join([chunk[1:] for chunk in chunks[:endIndex+1]]), 2)
            return Packet(version, id, value, []), binary
        else: #operator packet
            subpackets = []
            length, binary = binary[0], binary[1:]
            if length == '0':
                totalLength, binary = int(''.join(binary[:15]), 2), binary[15:]
                sub, binary = binary[:totalLength], binary[totalLength:]
                while sub:
                    packet, sub = Packet.parsePacket(sub)
                    subpackets.append(packet)
            else:
                numSubs, binary = int(''.join(binary[:11]), 2), binary[11:]
                for _ in range(numSubs):
                    packet, binary = Packet.parsePacket(binary)
                    subpackets.append(packet)
            return Packet(version, id, 0, subpackets), binary

hexi = open('in/16.txt').read()
binary = ''.join([bin(int(c, 16))[2:].zfill(4) for c in hexi])
packet, _ = Packet.parsePacket(binary)
print('part1:', packet.sumVersions())
print('part2:', packet.getValue())
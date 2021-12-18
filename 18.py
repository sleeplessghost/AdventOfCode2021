from math import ceil

class SnailNum:
    leftVal = 0
    rightVal = 0
    leftSnail = None
    rightSnail = None
    dirty = False

    def explode(self, depth):
        if depth >= 4 and not self.leftSnail and not self.rightSnail:
            return ('ex', self.leftVal, self.rightVal)
        else:
            result = None
            if self.leftSnail:
                result = self.leftSnail.explode(depth + 1)
                if result:
                    type, left, right = result
                    if type == 'ex':
                        self.leftSnail = None
                        self.leftVal = 0
                        self.dirty = True
                        if not self.rightSnail:
                            self.rightVal += right
                            result = (type, left, 0)
                        else:
                            right = self.rightSnail.setRight(right)
                            self.rightSnail.dirty = True
                            result = (type, left, right)
            if self.rightSnail and not result:
                result = self.rightSnail.explode(depth + 1)
                if result:
                    type, left, right = result
                    if type == 'ex':
                        self.rightSnail = None
                        self.rightVal = 0
                        self.dirty = True
                        if not self.leftSnail:
                            self.leftVal += left
                            result = (type, 0, right)
                        else:
                            left = self.leftSnail.setLeft(left)
                            self.leftSnail.dirty = True
                            result = (type, left, right)
            if result:
                type, left, right = result
                if type != 'ex':
                    self.dirty = True
                    if self.leftSnail:
                        left = self.leftSnail.setLeft(left)
                        self.leftSnail.dirty = True
                    else:
                        self.leftVal += left
                        left = 0
                    if self.rightSnail:
                        right = self.rightSnail.setRight(right)
                        self.rightSnail.dirty = True
                    else:
                        self.rightVal += right
                        right = 0
                result = ('set', left, right)
            return result

    def setRight(self, right):
        if self.dirty or right == 0: return right
        if not self.leftSnail:
            self.leftVal += right
            return 0
        right = self.leftSnail.setRight(right)
        if not self.rightSnail:
            self.rightVal += right
            return 0
        right = self.rightSnail.setRight(right)
        return right
    
    def setLeft(self, left):
        if self.dirty or left == 0: return left
        if not self.rightSnail:
            self.rightVal += left
            return 0
        left = self.rightSnail.setLeft(left)
        if not self.leftSnail:
            self.leftVal += left
            return 0
        left = self.leftSnail.setLeft(left)
        return left

    def split(self):
        if self.leftSnail and self.leftSnail.split(): return True
        if self.leftVal >= 10:
            num = SnailNum()
            num.leftVal = self.leftVal // 2
            num.rightVal = ceil(self.leftVal / 2.0)
            self.leftVal = 0
            self.leftSnail = num
            return True
        if self.rightSnail and self.rightSnail.split(): return True
        if self.rightVal >= 10:
            num = SnailNum()
            num.leftVal = self.rightVal // 2
            num.rightVal = ceil(self.rightVal / 2.0)
            self.rightVal = 0
            self.rightSnail = num
            return True
        return False
        
    def clean(self):
        self.dirty = False
        if self.leftSnail: self.leftSnail.clean()
        if self.rightSnail: self.rightSnail.clean()

    def magnitude(self):
        left, right = self.leftVal, self.rightVal
        if self.leftSnail: left = self.leftSnail.magnitude()
        if self.rightSnail: right = self.rightSnail.magnitude()
        return 3 * left + 2 * right

    def copy(self):
        result = SnailNum()
        result.leftVal = self.leftVal
        result.rightVal = self.rightVal
        if self.leftSnail: result.leftSnail = self.leftSnail.copy()
        if self.rightSnail: result.rightSnail = self.rightSnail.copy()
        return result

    def pr(self):
        s = "["
        if self.leftSnail: s += self.leftSnail.pr()
        else: s += str(self.leftVal)
        s += ","
        if self.rightSnail: s += self.rightSnail.pr()
        else: s += str(self.rightVal)
        s += "]"
        return s

def parseSnailNum(line):
    sub = line[1:-1]
    middle = findIndex(sub)
    left, right = sub[:middle], sub[middle+1:]
    num = SnailNum()
    if '[' not in left: num.leftVal = int(left)
    else: num.leftSnail = parseSnailNum(left)
    if '[' not in right: num.rightVal = int(right)
    else: num.rightSnail = parseSnailNum(right)
    return num

def findIndex(line):
    count = 0
    for i,c in enumerate(line):
        if c == '[': count += 1
        elif c == ']': count -= 1
        elif c == ',' and count == 0: return i

def add(snailA, snailB):
    result = SnailNum()
    result.leftSnail = snailA
    result.rightSnail = snailB
    return result

numbers = [parseSnailNum(x.strip()) for x in open('in/18.txt')]
total = numbers[0]
for n in numbers[1:]:
    total = add(total, n)
    doing = True
    while(doing):
        total.clean()
        if total.explode(0): continue
        if total.split(): continue
        doing = False

print('part1:', total.magnitude())

numbers = [parseSnailNum(x.strip()) for x in open('in/18.txt')]
magnitudes = []
for i,n in enumerate(numbers):
    for j,adder in enumerate(numbers):
        if i == j: continue
        total = add(n.copy(), adder.copy())
        doing = True
        while(doing):
            total.clean()
            if total.explode(0): continue
            if total.split(): continue
            doing = False
        magnitudes.append(total.magnitude())

print('part2:', max(magnitudes))
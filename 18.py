from math import ceil

class SnailNum:
    leftVal, rightVal, leftSnail, rightSnail, dirty = 0, 0, None, None, False

    def hasChildren(self): return self.leftSnail != None or self.rightSnail != None

    def explode(self, depth):
        if depth >= 3:
            if self.leftSnail:
                if not self.leftSnail.hasChildren():
                    left, right = self.leftSnail.leftVal, self.leftSnail.rightVal
                    self.leftVal, self.leftSnail = 0, None
                    if self.rightSnail: self.rightSnail.setRight(right)
                    else: self.rightVal += right
                    self.dirty = True
                    return (left, 0)
            elif self.rightSnail:
                if not self.rightSnail.hasChildren():
                    left, right = self.rightSnail.leftVal, self.rightSnail.rightVal
                    self.rightVal, self.rightSnail = 0, None
                    self.leftVal += left
                    self.dirty = True
                    return (0, right)
        result = None
        if self.leftSnail and not result: result = self.leftSnail.explode(depth + 1)
        if self.rightSnail and not result: result = self.rightSnail.explode(depth + 1)
        if result and result != (0,0):
            left, right = result
            if self.leftSnail: left = self.leftSnail.setLeft(left)
            else:
                self.leftVal += left
                left = 0
            if self.rightSnail: right = self.rightSnail.setRight(right)
            else:
                self.rightVal += right
                right = 0
            self.dirty = True
            result = (left,right)
        return result

    def setRight(self, right):
        if self.dirty or right == 0: return right
        if self.leftSnail: self.leftSnail.setRight(right)
        else: self.leftVal += right
        return 0
    
    def setLeft(self, left):
        if self.dirty or left == 0: return left
        if self.rightSnail: self.rightSnail.setLeft(left)
        else: self.rightVal += left
        return 0

    def split(self):
        if self.leftSnail and self.leftSnail.split(): return True
        if self.leftVal >= 10:
            num = SnailNum()
            num.leftVal, num.rightVal = self.leftVal // 2, ceil(self.leftVal / 2.0)
            self.leftVal, self.leftSnail = 0, num
            return True
        if self.rightSnail and self.rightSnail.split(): return True
        if self.rightVal >= 10:
            num = SnailNum()
            num.leftVal, num.rightVal = self.rightVal // 2, ceil(self.rightVal / 2.0)
            self.rightVal, self.rightSnail = 0, num
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
        result.leftVal, result.rightVal = self.leftVal, self.rightVal
        if self.leftSnail: result.leftSnail = self.leftSnail.copy()
        if self.rightSnail: result.rightSnail = self.rightSnail.copy()
        return result

def parseSnailNum(line):
    sub = line[1:-1]
    middle = findMiddle(sub)
    left, right = sub[:middle], sub[middle+1:]
    num = SnailNum()
    if '[' not in left: num.leftVal = int(left)
    else: num.leftSnail = parseSnailNum(left)
    if '[' not in right: num.rightVal = int(right)
    else: num.rightSnail = parseSnailNum(right)
    return num

def findMiddle(line):
    count = 0
    for i,c in enumerate(line):
        if c == '[': count += 1
        elif c == ']': count -= 1
        elif c == ',' and count == 0: return i

def add(snailA, snailB):
    result = SnailNum()
    result.leftSnail = snailA.copy()
    result.rightSnail = snailB.copy()
    while result.clean() or result.explode(0) or result.split(): pass
    return result

numbers = [parseSnailNum(x.strip()) for x in open('in/18.txt')]

total = numbers[0]
for n in numbers[1:]: total = add(total, n)
print('part1:', total.magnitude())

magnitudes = [add(a,b).magnitude() for i,a in enumerate(numbers) for j,b in enumerate(numbers) if i != j]
print('part2:', max(magnitudes))
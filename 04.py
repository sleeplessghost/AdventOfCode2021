MARKED = 'X'

def parseBoard(text):
    return [x.strip().split() for x in text.split('\n')]

def markNumber(board, number):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == number: board[y][x] = MARKED

def isComplete(board):
    columns = [[row[i] for row in board] for i in range(len(board[0]))]
    return any(isBingo(row) for row in board) or any(isBingo(col) for col in columns)

def isBingo(line):
    return all(x == MARKED for x in line)

def sumBoard(board):
    return sum(int(value) for row in board for value in row if value != MARKED)

def completeAllBoards(numbers, boards):
    complete = []
    incomplete = [*boards]
    for n in numbers:
        for board in incomplete:
            markNumber(board, n)
            if isComplete(board): complete.append((board, n))
        incomplete = [b for b in incomplete if not isComplete(b)]
        if len(incomplete) == 0: return complete

inputs = open('in/04.txt').read().split('\n\n')
numbers = inputs[0].split(',')
boards = [parseBoard(b) for b in inputs[1:]]
completed = completeAllBoards(numbers, boards)

(winner, numA), (last, numB) = completed[0], completed[-1]
print('part1:', sumBoard(winner) * int(numA))
print('part2:', sumBoard(last) * int(numB))
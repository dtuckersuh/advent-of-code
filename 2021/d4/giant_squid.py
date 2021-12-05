def read_input():
    with open('input.txt') as f:
        boards = []
        numbers = [num.strip() for num in f.readline().split(",")]
        currentBoard = []
        next(f)
        for line in f:
            if line == '\n':
                boards.append(currentBoard)
                currentBoard = []
            else:
                currentBoard.append(line.strip().split())
        boards.append(currentBoard)
        return(numbers, boards)   

numbers, boards = read_input()

def bingo():
    # For each num drawn, mark num on each board
    lastBoardWon = []
    lastNum = 0 
    for num in numbers:
        for board in list(boards):
            board = markBoard(board, num)
            if checkBoard(board):
                # Part 2: Remove board when it wins
                lastBoardWon = board 
                lastNum = int(num)
                boards.remove(board)
                #sum = sumBoard(board)
                #return sum * int(num)
    sum = sumBoard(lastBoardWon)
    return sum * int(lastNum) 

# Return marked board w/ drawn num == 1 
def markBoard(board, num):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == num:
                board[row][col] = 'mark'
    return board

# Return sum of all unmarked numbers on board
def sumBoard(board):
    sum = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != 'mark':
                sum += int(board[row][col])
    return sum

# Return whether board is a winner
def checkBoard(board):
    for row in range(len(board)):
        if checkHorizontal(board, row):
            return True
    for col in range(len(board[0])):
        if checkVertical(board, col):
            return True
    return False      

# Check if given row is all marked
def checkHorizontal(board, row):
    for col in range(len(board[0])):
        if board[row][col] != 'mark':
            return False
    return True

# Check if given column is all marked
def checkVertical(board, col):
    for row in range(len(board)):
        if board[row][col] != 'mark':
            return False
    return True

print(bingo())

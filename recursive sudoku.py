# soduku solver
# created by Austin Swarltey on 1/9/25

# goal in first iteration of development is for the program to solve any valid sudoku puzzle on a command line interface.

# future goals: 
# - manual solving
# - visualize the algirithm as it works
# - boxes around the 
# - GUI interface insead of command line

import math 

def printBoard(board):
    boxLen = int(math.sqrt(len(board[0])))
    for i in range(len(board)):
        if i % boxLen == 0 and i != 0:
            print("-" * ((len(board))*boxLen + 1))
        for j in range(len(board[0])):
            if j % boxLen == 0 and j != 0:
                print("| ", end="")
            if j == len(board) - 1:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
        
def isValid():
    pass

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j) # row, col 

if __name__ == '__main__':
    board = [
            [0,1,0,0],
            [2,0,0,0],
            [0,0,3,0],
            [0,0,0,4]]
    empty = findEmpty(board)
    print(empty)
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
    #prints a passed in sudoku board. board is represented by a 2D list
    for row in board:
        # save below if i add command line 
        #rowLength = len(row)
        #boxes = int(math.sqrt(rowLength)) # will always be valid by the nature of sudoku 
        for idx in range(0,len(row)):
            
            print(row[idx], end=" ")
        print()

def isValid():
    pass
if __name__ == '__main__':
    board = [[0, 1, 0, 0], [2, 0, 0, 0], [0,0,0,0],[0,0,0,0]]
    printBoard(board)
# soduku solver
# created by Austin Swarltey on 1/9/25

# goal in first iteration of development is for the program to solve any valid sudoku puzzle on a command line interface.
# assumes 3x3 board

# future goals: 
# - generate a valid starting board
# - manual solving
# - visualize the algirithm as it works
# - GUI interface insead of command line

import math 

the_board = [[0,0,0,0,0,0,0,0,0,],
             [0,0,0,0,0,0,0,0,0,],
             [0,0,0,0,0,0,0,0,0,],
             [0,0,0,0,0,0,0,0,0,],
             [0,0,0,0,0,0,0,0,0,],
             [0,0,0,0,0,0,0,0,0,],
             [0,0,0,0,0,0,0,0,0,],
             [0,0,0,0,0,0,0,0,0,],
             [0,0,0,0,0,0,0,0,0,]]

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * ((len(board))*2 + 3))
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == len(board) - 1:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")    

def isValid(board, num, pos):
    #check row
    for i in range (len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, (box_x*3 + 3)):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def findEmpty(board):
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            if board[i][j] == 0:
                return (i, j) # row, col 
    return None               #for base case

def solve(board):
    pos = findEmpty(board)
    if not pos:
        return True
    else:
        row, col = pos

    for i in range(1, len(board) + 1):
        if isValid(board, i, (row,col)):
            board[row][col] = i
            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False

if __name__ == '__main__':
    printBoard(the_board)
    solve(the_board)
    print()
    print()
    print()
    printBoard(the_board)
      
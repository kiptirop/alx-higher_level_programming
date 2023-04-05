#!/usr/bin/python3

"""A program that solves the Nqueens problem"""

import sys

def nqueens(N):
    """Initializes an n x n sized chessboard"""
    # Check that N is a positive integer greater than or equal to 4
    try:
        N = int(N)
        if N < 4:
            raise ValueError
    except ValueError:
        print("N must be a number greater than or equal to 4")
        sys.exit(1)
    
    # Initialize the board to be a list of N lists, each with N zeros
    board = [[0]*N for _ in range(N)]
    
    # Define a helper function to check if a given placement of queens is valid
    def is_valid(board, row, col):
        """checks the if valid before it returns"""
        # Check the row
        if 1 in board[row]:
            return False
        
        # Check the column
        for i in range(N):
            if board[i][col] == 1:
                return False
        
        # Check the diagonal
        for i in range(N):
            for j in range(N):
                if (i + j == row + col) or (i - j == row - col):
                    if board[i][j] == 1:
                        return False
        
        # If we made it here, the placement is valid
        return True
    
    # Define a recursive function to try all possible placements of queens
    def solve(board, row):
        """Returns the list representation of a solved chessboard"""
        # If we've placed a queen in every row, we have a solution!
        if row == N:
            for row in board:
                print(' '.join(str(x) for x in row))
            print()
            return
        
        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_valid(board, row, col):
                board[row][col] = 1
                solve(board, row+1)
                board[row][col] = 0
    
    # Start the recursive search from the first row
    solve(board, 0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        nqueens(sys.argv[1])


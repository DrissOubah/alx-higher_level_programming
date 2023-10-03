#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty cells."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board


def is_safe(board, row, col):
    """Check if it's safe to place a queen at a given position."""
    # Check the row
    if 'Q' in board[row]:
        return False

    # Check the column
    if 'Q' in [board[i][col] for i in range(len(board))]:
        return False

    # Check the diagonal (up-left to down-right)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check the diagonal (up-right to down-left)
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False

    return True


def recursive_solve(board, row, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        solutions (list): A list of solutions.
    Returns:
        solutions
    """
    if row == len(board):
        solutions.append(get_solution(board))
        return solutions

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'
            solutions = recursive_solve(board, row + 1, solutions)
            board[row][col] = ' '  # Backtrack

    return solutions


def get_solution(board):
    """Return the solution as a list of [row, column] pairs."""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 'Q':
                solution.append([row, col])
    return solution


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = recursive_solve(board, 0, [])
    for sol in solutions:
        print(sol)

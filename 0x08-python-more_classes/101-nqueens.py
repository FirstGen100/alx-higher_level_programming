#!/usr/bin/python3
import sys

def reject_squares(board):
    for cols in board:
        for col_b in board:
            if not cols is col_b:
                if cols[0] == col_b[0]:
                    return True
                if cols[1] == col_b[1]:
                    return True
                if cols[0] + cols[1] == col_b[0] + col_b[1]:
                    return True
    return False

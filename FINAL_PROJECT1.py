# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 19:15:32 2024

@author: APBaker
"""

import streamlit as st
import time

def intro():
    st.title("Welcome to Allie's Tic Tac Toe Game!")
    st.write("Rules: Players, represented by X and O, will take turns putting their marks in the empty squares below. The first player to get 3 of their marks in a row either vertically, horizontally, or diagonally, is the winner! If all 9 squares are full, and no player has 3 in a row, then the game is a tie.")
    st.write("Let's get started!")

def create_grid():
    st.write("Here is the playboard:")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board

def sym():
    symbol_1 = st.selectbox("Player 1, do you want to be X or O?", ["X", "O"])
    symbol_2 = "O" if symbol_1 == "X" else "X"
    st.write(f"Player 2, you are {symbol_2}.")
    return(symbol_1, symbol_2)

def print_pretty(board):
    rows = len(board)
    cols = len(board)
    pretty_board = ""
    pretty_board += "---+---+---\n"
    for r in range(rows):
        pretty_board += f"{board[r][0]} | {board[r][1]} | {board[r][2]}\n"
        pretty_board += "---+---+---\n"
    st.text(pretty_board)

def start_gaming(board, symbol_1, symbol_2, count):
    if count % 2 == 0:
        player_symbol = symbol_2
    else:
        player_symbol = symbol_1
    st.write(f"Player {player_symbol}, it's your turn.")
    row = st.selectbox("Pick a row", [0, 1, 2], key=f"row_{count}_{player_symbol}")
    col = st.selectbox("Pick a column", [0, 1, 2], key=f"col_{count}_{player_symbol}")
    return (row, col)

def is_winner(board, symbol_1, symbol_2):
    winner = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol_1 or \
           board[i][0] == board[i][1] == board[i][2] == symbol_2 or \
           board[0][i] == board[1][i] == board[2][i] == symbol_1 or \
           board[0][i] == board[1][i] == board[2][i] == symbol_2:
            winner = True
            break
    if board[0][0] == board[1][1] == board[2][2] == symbol_1 or \
       board[0][0] == board[1][1] == board[2][2] == symbol_2 or \
       board[0][2] == board[1][1] == board[2][0] == symbol_1 or \
       board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = True
    return winner

def is_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def illegal(board, row, col):
    return board[row][col] != " "

def main():
    intro()
    board = create_grid()
    symbol_1, symbol_2 = sym()
    count = 1
    winner = False

    while count <= 9 and not winner:
        print_pretty(board)
        row, col = start_gaming(board, symbol_1, symbol_2, count)
        while row > 2 or row < 0 or col > 2 or col < 0:
            st.error("Out of boarder. Pick another one.")
            row, col = start_gaming(board, symbol_1, symbol_2, count)
        while illegal(board, row, col):
            return st.error("The square you picked is already filled. Pick another one.")

        if count % 2 == 0:
            player = symbol_2
        else:
            player = symbol_1

        board[row][col] = player
        if is_winner(board, symbol_1, symbol_2):
            winner = True
            st.success(f"Player {player} wins! Refresh the page to play again!")
            time.sleep(1)
            st.balloons()
            print_pretty(board)
        count += 1

    if not winner:
        st.warning("It's a tie! Refresh the page to play again!")

if __name__ == "__main__":
    main()












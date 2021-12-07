# your code goes here
import string
import random
import os
import sys
import time
import numpy as np
from IPython.display import clear_output

def ChessBoardSetup():
    b = np.array([['r','t','b','q','k','b','t','r'],
                  ['p','p','p','p','p','p','p','p'],
                  ['.','.','.','.','.','.','.','.'],
                  ['.','.','.','.','.','.','.','.'],
                  ['.','.','.','.','.','.','.','.'],
                  ['.','.','.','.','.','.','.','.'],
                  ['P','P','P','P','P','P','P','P'],
                  ['R','T','B','Q','K','B','T','R'],
    ])
    return b

def DrawBoard(Board):
    print(Board, end="\n\n")

def MovePiece(board, from_piece, to_piece):
    board[to_piece[0], to_piece[1]] = board[from_piece[0], from_piece[1]]
    board[from_piece[0], from_piece[1]] = '.'
    return board

def IsMoveLegal(board, from_square, to_square):
    if board[from_square[0], from_square[1]] == board[to_square[0], to_square[1]]:
        return False

    # Check if the board has a piece that is a pawn
    elif(board[from_square[0], from_square[1]] == 'p'):
        if(board[to_square[0],to_square[1]] == '.' and board[to_square[1]] == board[from_square[1]]):
            return True
        elif(board[to_square[0], to_square[1]] == '.' and board[from_square[0]] == 2 and board[from_square[0]] == board[from_square[0]] + 2):
            if IsClearPath(board,from_square,to_square):
                return True

    # Check if the board has a piece that is a rook
    elif(board[from_square[0],from_square[1]] == 'r'):
        if(board[to_square[0]] == board[from_square[0]] or board[to_square[1]] == board[from_square[1]]):
            if(board[to_square[0],to_square[1]] == '.' or (board[to_square[0],to_square[1]])).isupper(): # Empty or enemy pieces
                if IsClearPath(board,from_square,to_square):
                    return True

    # Check if the board has a piece that is a bishop
    # Double check this code
    elif(board[from_square[0],from_square[1]] == 'b'):
        if(abs(from_square[0] - to_square[0]) == abs(from_square[1] - to_square[1])):
            if(board[to_square[0],to_square[1]] == '.' or (board[to_square[0],to_square[1]]).isupper()): # Empty or Enemy Pieces
                if IsClearPath(board,from_square,to_square):
                    return True

    # Check if the board has a piece that is a Queen
    elif(board[from_square[0],from_square[1]] == 'q'):
        if(board[to_square[0]] == board[from_square[0]] or board[to_square[1]] == board[from_square[1]]):
            if(board[to_square[0],to_square[1]] == '.' or (board[to_square[0],to_square[1]]).isupper()): # Empty or Enemy Pieces
                if IsClearPath(board, from_square, to_square):
                    return True
        # Don't forget to implement the diagonal
        if(abs(from_square[0] - to_square[0]) == abs(from_square[1] - to_square[1])):
            if(board[to_square[0],to_square[1]] == '.' or (board[to_square[0],to_square[1]]).isupper()): # Empty or Enemy Pieces
                if IsClearPath(board,from_square,to_square):
                    return True

    # Check if the board has a piece that is a knight
    elif(board[from_square[0],from_square[1]] == 't'):
        row_diff == board[to_square[0]] - board[from_square[1]]
        col_diff == board[to_square[1]] - board[from_square[1]]
        if(board[to_square[0], to_square[1]] == '.' or  (board[to_square[0],to_square[1]]).isupper()):
            if col_diff == 1 and row_diff == -2:
                return True
            elif col_diff == 2 and row_diff == -1:
                return True
            elif col_diff == 1 and row_diff == 2:
                return True
            elif col_diff == -2 and row_diff == -1:
                return True
            elif col_diff == -2 and row_diff == 1:
                return True
            elif col_diff == -1 and row_diff == 2:
                return True

    # Check if the board has a piece that is a King
    elif(board[from_square[0],from_square[1]] == 'k'):
        row_diff == board[to_square[0]] - board[from_square[1]]
        col_diff == board[to_square[1]] - board[from_square[1]]
        if(board[to_square[0],to_square[1]] == '.' or (board[to_square[0],to_square[1]]).isupper()):
            if(abs(col_diff) == 1 and abs(row_diff) == 0):
                return True
            elif(abs(col_diff) == 0 and abs(row_diff) == 1):
                return True
            elif(abs(col_diff) == 1 and abs(row_diff) == 1):
                return True
        else:
            return False

# gets a list of legal moves for a given piece
# input = from-square
# output = list of to-square locations where the piece can move to
def GetListOfLegalMoves(board, from_square, to_square):
    # input is the current player and the given piece as the from-square
    # initialize the list of legal moves, i.e., to-square locations to []
    legal_moves = []
    # go through all squares on the board
    # for the selected square as to-square
    for to_square in range(0, rows):
        for to_square in range(0, cols):
            # call IsMoveLegal() with input as from-square and to-square and save the returned value
            legal = IsMoveLegal(board, from_square, to_square)
            if board.legal == True:
            # if returned value is True
                # call DoesMovePutPlayerInCheck() with input as from-square and to-square and save the returned value
                inCheck = DoesMovePutPlayerInCheck(board, from_square, to_square)
                if board.inCheck() == False:
                # if returned value is False
                    # append this move (to-square) as a legal move
                    legal_moves.append[to_square[0],to_square[1]]
        # return the list of legal moves, i.e., to-square locations
    return legal_moves

# gets a list of all pieces for the current player that have legal moves
def GetPiecesWithLegalMoves():
    # initialize the list of pieces with legal moves to []
    legal = []
    # go through all squares on the board
    # for the selected square
    for to_square in range(0, rows):
        for to_square in range(0, cols):
        # if the square contains a piece that belongs to the current player's team
            if to_square == ('p' or 'r' or 't' or 'b' or 'q' or 'k'):#piece that belongs to the current player's team
            # call GetListOfLegalMoves() to get a list of all legal moves for the selected piece / square
                legal_list = GetListOfLegalMoves(board, from_square, to_square)
            # if there are any legal moves
                if legal_list == True:
                # append this piece to the list of pieces with legal moves
                    legal.append(legal_list)
    # return the final list of pieces with legal moves
    return legal

# returns True if the current player is in checkmate, else False
def IsCheckmate():
    # call GetPiecesWithLegalMoves() to get all legal moves for the current player
    GetPiecesWithLegalMoves()
    # if there is no piece with any valid move
    if board.GetPiecesWithLegalMoves() == False:
        return False
    else:
        return True


# Figure out if a move is legal for straight-line moves
# returns true if the path is clear for a mov
def IsClearPath(board, from_square, to_square):
    row_diff == board[to_square[0]] - board[from_square[1]]
    col_diff == board[to_square[1]] - board[from_square[1]]
    if(col_diff <= 1 and col_diff >= -1) and (row_diff <= 1 and row_diff >= -1):
        return True
    else:
        if(board[from_square[1]] == board[to_square[1]]) and (board[from_square[0]] <= board[to_square[0]]):
            from_new_square = board[to_square[0]]
        elif(board[from_square[1]] == board[from_square[1]] and board[from_square[0]] >= board[to_square[0]]):
            from_new_square = board[to_square[0]]
        elif(board[from_square[0]] == board[to_square[0]] and board[from_square[1]] <= board[to_square[1]]):
            new_from_square = board[to_square[1]]
        elif(board[from_square[0]] == board[to_square[0]] and board[from_square[1]] >= board[to_square[1]]):
            new_from_square = board[to_square[1]]
        elif(board[from_square[0]] >= board[to_square[0]] and board[from_square[1]] >= board[to_square[1]]):
            new_from_square = board[to_square[0][1]]
        elif(board[from_square[0]] >= board[to_square[0]] and board[from_square[1]] <= board[to_square[1]]):
            new_from_square = board[to_square[0][1]]
        elif(board[from_square[0]] <= board[to_square[0]] and board[from_square[1]] >= board[to_square[1]]):
            new_from_square = board[to_square[0][1]]
        elif(board[from_square[0]] <= board[to_square[0]] and board[from_square[1]] <= board[to_square[1]]):
            new_from_square = board[to_square[0][1]]
    if(new_from_square != '.'):
        return False
    else:
        return new_from_square, to_square

# Returns true if the given player is in check state
def IsInCheck(board,from_square,king_square):
    if(board[king_square[0][1]]) == 'k':
        king_coords = king_square[0][1]
    else:
        king_coords = king_square[0][1]

    for row in board:
        for piece in row:
            if board.IsMoveLegal(board,from_square,king_square) == True:
                return True
            else:
                continue
    return False

# makes a hypothetical move (from-square and to-square)
# returns True if it puts current player into check
#def DoesMovePutPlayerInCheck(board, from_square, king_square):
    # given the move (from-square and to-square), find the 'from-piece' and 'to-piece'
    # make the move temporarily by changing the 'board'
    # Call the IsInCheck() function to see if the 'player' is in check - save the returned value
    # Undo the temporary move
    # return the value saved - True if it puts current player into check, False otherwise
#    king_coords = None
#    if type(board[from_square[0][1]]) == 'k':

def GetRandomMove():
    # pick a random piece and a random legal move for that piece
    moves = GetPiecesWithLegalMoves()
    if moves:
        return random.choice(moves)

# this function will calculate the score on the board, if a move is performed
# give score for each of piece and calculate the score for the chess board
# Upper-case is white
# Lower-case is black
def boardEval(board):
    score = 0
    for row in board:
        for piece in row:
            if piece != '.':
                if piece == 'K':
                    score += 100
                elif piece == 'k':
                    score -= 100
                elif piece == 'Q':
                    score += 9
                elif piece == 'q':
                    score -= -9
                elif piece == 'R':
                    score += 5
                elif piece == 'r':
                    score -= 5
                elif piece == 'T':
                    score += 3
                elif piece == 't':
                    score -= -3
                elif piece == 'B':
                    score += 3
                elif piece == 'b':
                    score -= 3
                elif piece == 'P':
                    score += 1
                elif piece == 'p':
                    score -= 1
    return score


def minimax(board, depth, maximizing_player, maximizing_color):
    # return the best move for the current player using the MinMax strategy
    # to get the allocated points, searching should be 2-ply (one Max and one Min)
    if depth == 0:
        return None, evl(board, maximizing_color)
    moves = board.GetRandomMove()
    best_move = random.choice(moves)

    if maximizing_player:
        max_eval = -inf
        for move in moves:
            board.MovePiece(board, move[0], move[1])
            current_eval = minimax(board, depth - 1, alpha, beta, False, maximizing_color)[1]
            if current_eval > max_eval:
                max_eval = current_eval
                best_move = move
        return best_move, max_eval
    else:
        min_eval = inf
        for move in moves:
            board.MovePiece(board, move[0], move[1])
            current_eval = minimax(board, depth - 1, alpha, beta, True, maximizing_color)[1]
            if current_eval < min_eval:
                min_eval = current_eval
                best_move = move
        return best_move, min_eval

# initialize and setup the board
# player assignment and counter initializations

# main game loop - while a player is not in checkmate or stalemate (<N turns)
# below is the rough looping strategy
while not IsCheckmate() and turns < N:
    clear_output()
    myBoard = ChessBoardSetup()
    DrawBoard(myBoard)

    # write code to take turns and move the pieces
    DrawBoard(board)
    time.sleep(0.5)

# check and print - Stalemate or Checkmate
while not IsCheckMate() and turns < N:
    clear_output()
    myBoard = ChessBoardSetup()
    DrawBoard(myBoard)

    #Write code to take turns and move the pieces
    MovePiece(myBoard, [1,2], [3,2]) # Move Pawn two spaces forward
    DrawBoard(myBoard)
    MovePiece(myBoard, [7,7], [5,6]) # Move Rook two space up, 1 left over
    DrawBoard(myBoard)

    # Check and print - stalemate or checkmate

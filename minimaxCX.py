#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:33:04 2020

@author: michaelsteinberg
"""
import numpy as np
import time
import math

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = np.zeros((6, 7), dtype = np.int32)
        self.move_count = 0

        # Player X always plays first
        self.player_turn = 1

    def draw_board(self):
        for i in range(0, 6):
            for j in range(0, 7):
                token = self.current_state[i][j]
                if token == -1:
                    token = 'X'
                elif token == 1:
                    token = 'O'
                else:
                    token = '.'
                print('{}|'.format(token), end=" ")
            print()
        print()
        
    
    # Determines if the made move is a legal move
    def is_valid(self, px):
        if px < 0 or px > 6:
            return False
        elif int(self.current_state[0][px]) != 0:
            return False
        else:
            return True
        
        
    def get_boxes(self, player=1):
        boxes = []
        for i in range(3):
            for j in range(4):
                boxes.append(self.current_state[i:4 + i, j:4 + j])
        return boxes
    
    def check_columns(self, player=1):
        for box in self.get_boxes():
            for i in range(4):
                if (np.all(box.T[i] == player)):
                    return True
        return False
    
    def check_rows(self, player=1):
        for box in self.get_boxes():
            for i in range(4):
                if (np.all(box[i] == player)):
                    return True
        return False
    
    def check_diag_1(self, player=1):
        diagonal = []
        for box in self.get_boxes():
            for i in range(4):
                diagonal.append(box[i, i])
            if (np.all(np.array(diagonal) == player)):
                    return True
            diagonal.clear()
        return False

    
    def check_diag_2(self, player=1):
        diagonal = []
        for box in self.get_boxes():
            for i in range(4):
                diagonal.append(box[i, -(i + 1)])
            if (np.all(np.array(diagonal) == player)):
                return True
            diagonal.clear()
        return False
            
    def check_board_full(self, player=1):
        for i in range(0, 6):
            for j in range(0, 7):
                if self.current_state[i, j] == 0:
                    return False
        return True
    
    # The game is over
    def is_end(self):
        if self.check_columns() or self.check_rows() or self.check_diag_1() or self.check_diag_2():
            return 1
        elif self.check_columns(-1) or self.check_rows(-1) or self.check_diag_1(-1) or self.check_diag_2(-1):
            return -1
        elif self.check_board_full():
            return 0
        else:
            return

    def drop_token(self, column, player):
        if self.is_valid(column):
            # If all the values in this column of the current state are 0, make the bottom value a 1
            if (np.all(np.array(self.current_state.T[column]) == 0)):
                self.current_state[-1][column] = player
                return
                
            # Otherwise
            for row in range(self.current_state.shape[0] - 1):
                if int(self.current_state[row + 1][column]) != 0:
                    self.current_state[row][column] = player
                    return

    # Player 'O' is max, in this case AI
    def max_state(self, alpha, beta, curr_depth=0):
    
        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        #print("max_called")
    
        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2
    
        px = None
    
        result = self.is_end()
    
        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == -1:
            return (-1, 0)
        elif result == 1:
            return (1, 0)
        elif result == 0 or curr_depth > 2 + math.pow(self.move_count, (1/3)):
            return (0, 0)
    
        # Check all the potential moves 
        for i in range(0, 7):
            if self.is_valid(i):

                # On the empty field player 'O' makes a move and calls Min
                # That's one branch of the game tree.
                old_state = self.current_state.copy()
                self.drop_token(i, player=1)
                #print(self.min_state())
                (m, min_i) = self.min_state(alpha, beta, curr_depth + 1)
                # Fixing the maxv value if needed
                if m > maxv:
                    maxv = m
                    px = i
                    
                    
                if maxv >= beta:
                    return (maxv, px)

                if maxv > alpha:
                    alpha = maxv

                # Setting back the field to empty
                self.current_state = old_state
        return (maxv, px)


    # Player -1 is min, in this case human
    def min_state(self, alpha, beta, curr_depth=0):
    
        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        #print("min_called")
    
        # We're initially setting it to -2 as worse than the worst case:
        minv = 2
    
        qx = None
    
        result = self.is_end()
    
        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == -1:
            return (-1, 0)
        elif result == 1:
            return (1, 0)
        elif result == 0 or curr_depth > 2 + math.pow(self.move_count, (1/3)):
            return (0, 0)
    
        # Check all the potential moves 
        for i in range(0, 7):
            if self.is_valid(i):
                #print("Valid move")
                # On the empty field player 'O' makes a move and calls Min
                # That's one branch of the game tree.
                old_state = self.current_state.copy()
                self.drop_token(i, player=-1)
                (m, max_i) = self.max_state(alpha, beta, curr_depth + 1)
                # Fixing the maxv value if needed
                if m < minv:
                    minv = m
                    qx = i
                
                if minv <= alpha:
                    return (minv, qx)

                if minv < beta:
                    beta = minv
                # Setting back the field to empty
                self.current_state = old_state 
            else:
                pass
                #print("invalid move")
        return (minv, qx)
    
    
    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_end()
    
            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == -1:
                    print('The winner is X!')
                elif self.result == 1:
                    print('The winner is O!')
                elif self.result == 0:
                    print("It's a tie!")
    
                self.initialize_game()
                return
    
            # If it's player's turn
            if self.player_turn == -1:
    
                while True:
    
                    start = time.time()
                    (m, qx) = self.min_state(-2, 2)
                    if m == 1: 
                        #print("X is without hope")
                        pass
                    elif m == -1:
                        pass
                        #print("X has found a winning move")
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: column = {}'.format(qx))
    
                    #px = int(input('Insert the Column Coordinate: '))

                    #(qx) = (px)
    
                    if self.is_valid(qx):
                        self.drop_token(qx, -1)
                        self.player_turn = 1
                        break
                    else:
                        pass
                        print('The move is not valid! Try again.')
    
            # If it's AI's turn
            else:
                (m, px) = self.max_state(-2, 2)
                if m == 1:
                    print("O has found a winning move! {}".format(px))
                elif m == -1:
                    print("O is without hope")
                self.drop_token(px, 1)
                self.player_turn = -1

    def check_for_win_or_loss(self):
        
        # If we can win the game (Max Found = 1), then that is the
        # move we must make.
        old_state = self.current_state.copy()
        (m, px) = self.max_state(-2, 2)
        self.current_state = old_state
        if m == 1:
            #print("O has found a winning move! {}".format(px))
            return (1, px)
        elif m == -1: 
            #print("O is without hope")
            return (-1, px)
        else:
            #print("No Winning moves found")
            return (0, px)
        
        # If maxfound is 0, test to see if making a move leads to the 
        # opponent finding a win. If so, override the move. 
    
    def verify_move(self, move):
        old_state = self.current_state.copy()
        valid_move = self.is_valid(move)
        # If the move we selected is invalid, pick the best available move
        if not valid_move:
            (m, qx) = self.max_state(-2, 2)
            self.current_state = old_state
            return qx
        # If the move is valid, drop the token and see if it leads to a lost 
        # state if so, pick the best available move
        self.drop_token(move, 1)
        self.player_turn = -1
        (m, qx) = self.min_state(-2, 2)
        #print(m, "max val")
        if m == -1:
            self.move_count += 1
            #print("This Leads to a losing move! {}".format(qx))
            self.current_state = old_state
            self.player_turn = 1
            (m, qx) = self.max_state(-2, 2)
            #print("Selected a safe move, {}".format(qx))
            self.current_state = old_state
            return qx
        # If the move is safe, return this move. 
        else: 
            #print("No Move Danger detected")
            self.current_state = old_state
            self.player_turn = 1
            return move
            
    def make_board_from_observation(self, observation, opponent):
        board = np.array(observation)
        board = np.array(list(map(lambda x: x if x != opponent else -1, board)))
        board = board.reshape(6, 7)
        print(board)
        return board
        
    
    def make_opponent_move(self, observation, opponent):
        self.current_state = self.make_board_from_observation(observation, opponent)
        
        
        
    
        
        
g = Game()
g.check_for_win_or_loss()
g.verify_move(0)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:05:27 2020

@author: michaelsteinberg
"""
import numpy as np
import torch

class PreprocessBoard:
    
    def __init__(self, board_dims):
        
        self.board_dims = board_dims
        
        
    def create_board_observation(self, board):
        board = np.array(board)
        board = np.array(list(map(lambda x: x if x != 2 else -1, board)))
        board = board.reshape(self.board_dims[0], self.board_dims[1])
        board = np.expand_dims(board, axis=0)
        return torch.FloatTensor(board)
    
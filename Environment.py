#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:36:41 2020

@author: michaelsteinberg
"""


from kaggle_environments import evaluate, make, utils
import gym

env = make("connectx", debug=True)
env.specification.reward



# This agent random chooses a non-empty column.
def my_agent(observation, configuration):
    from random import choice
    return choice([c for c in range(configuration.columns) if observation.board[c] == 0])


env.reset()
env.run([my_agent, "random"])



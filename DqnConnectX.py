#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:34:54 2020

@author: michaelsteinberg
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:30:17 2020

@author: michaelsteinberg
"""


# AI for Self Driving Car

# Importing the libraries

import numpy as np
import random
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from preprocess_board import PreprocessBoard
# Creating the architecture of the Neural Network

### Part 1: Building a A Neural Network 

class CNN(nn.Module):
    
    def __init__(self, board_dims, nb_actions):
        
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=10, kernel_size = 3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=10, out_channels=8, kernel_size = 2, padding=1)
        self.fc1 = nn.Linear(in_features = self.count_neurons(board_dims), out_features = 40)
        self.fc2 = nn.Linear(in_features = 40, out_features = nb_actions)
        
    def count_neurons(self, board_dim):
        # Generate a fake board state
        x = torch.rand((1, 1, *board_dim))
        x = F.relu(F.max_pool2d(self.conv1(x), kernel_size=3, stride=2))
        x = F.relu(F.max_pool2d(self.conv2(x), kernel_size=3, stride=2))
        # Get the values from the tensor and put it into a numpy object, 
        # reshape to flatten and then get the size of the non batch dimension
        x = x.detach().numpy().reshape(1, -1)
        return x.shape[1]
        
    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), kernel_size=3, stride=2))
        x = F.relu(F.max_pool2d(self.conv2(x), kernel_size=3, stride=2))
        # Flatten it out so we can put it into the fcs 
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
        # Q values

# Implementing Experience Replay

class ReplayMemory(object):
    
    def __init__(self, capacity):
        # Number of elements that can fit in memory
        self.capacity = capacity
        # List Containing Memory. Each memory contains the
        # previous state, current state, the action taken between the states
        # and the reward
        self.memory = []
    
    def push(self, event):
        # Append the new memory to the memories list
        self.memory.append(event)
        # If we're over capacity delete the oldest memory
        if len(self.memory) > self.capacity:
            del self.memory[0]
    
    def sample(self, batch_size):
        # Obtains a list of tuples containing memories. Creates four lists
        # containing the old states, the new states, the actions and the
        # rewards
        samples = zip(*random.sample(self.memory, batch_size))
        # For every memory in the list, create a Torch variable
        # that can be used.
        # Create an iterator of tensors that can be passed in. 
        #batch1 = list(samples)[0]
        #for ten in batch1:
            #print(ten)
        return tuple(map(lambda x: torch.cat(x, 0), samples))

# Implementing Deep Q Learning

class Dqn():
    
    def __init__(self, board_dims, nb_action, gamma):
        self.gamma = gamma
        self.reward_window = []
        self.model = CNN(board_dims, nb_action)
        self.memory = ReplayMemory(100000)
        self.optimizer = optim.Adam(self.model.parameters(), lr = 0.001)
        self.last_state = torch.zeros((1, 1, board_dims[0], board_dims[1]), dtype=torch.float32)
        self.last_action = 0
        self.last_reward = 0
    
    def select_action(self, state):
        with torch.no_grad():
            probs = F.softmax(self.model(state) * 100, dim=1) # T=100
            # Select an action randomly based on 1 sample of this distrbution 
            action = probs.multinomial(num_samples = 1)
            # Action is a tensor containing one value so we detach it convert
            # to numpy and get the value out
            return action.detach().numpy()[0]
    
    def learn(self, batch_state, batch_next_state, batch_reward, batch_action):
        # Run a batch through the network and get the q value of the chosen
        # action from each state in the batch.
        # (Quality of actions given the state)
        # Here's what this line does:
            # First we get the q values for each batch state.
            # Gather selects based on the index given from batch_action. 
            # Essentially, the outputs are the one q value for the action that we selected. 
        outputs = self.model(batch_state).gather(1, batch_action.unsqueeze(1)).squeeze(1)
        # Get the max predicted q value of the next state
        # New Quality of the actions given the 
        # (Quality of the State given the actions)
        # So effectively we run our next state through the network to get
        # the quality of all the actions. The q-value of the max of these 
        # actions is part of the equation for calculating the value of the
        # state. This can be used to
        # determine the quality of the action that led to the state.
        next_outputs = self.model(batch_next_state).detach().max(1)[0]
        target = self.gamma*next_outputs + batch_reward
        td_loss = F.smooth_l1_loss(outputs, target)
        self.optimizer.zero_grad()
        td_loss.backward()
        self.optimizer.step()
    
    def update(self, reward, new_board_array):
        # Put the signal that we get in a tensor and add a dimension for the batch
        new_state = PreprocessBoard((6, 7)).create_board_observation(new_board_array).unsqueeze(0)
        # Push the state to our memory 
        self.memory.push((self.last_state, new_state, torch.LongTensor([int(self.last_action)]), torch.FloatTensor([self.last_reward])))
        # Select an action given our state
        action = self.select_action(new_state)
        # Once we have enough elements in our memory we have the ability to begin learning. 
        if len(self.memory.memory) > 100:
            batch_state, batch_next_state, batch_action, batch_reward = self.memory.sample(100)
            # we learn in batches as gradient descent is inherently more stable this way. 
            self.learn(batch_state, batch_next_state, batch_reward, batch_action)
        # Update the last action to be the current action we just took
        self.last_action = action
        # Update the last state to be the state we just took. 
        self.last_state = new_state
        # Update the last reward to be the new reward
        self.last_reward = reward
        # Add the reward to the reward window
        self.reward_window.append(reward)
        if len(self.reward_window) > 1000:
            # If we've reached an amount of rewards that's too large get rid of the oldest reward. 
            del self.reward_window[0]
        return action
    
    def score(self):
        return sum(self.reward_window)/(len(self.reward_window)+1.)
    
    def save(self):
        torch.save({'state_dict': self.model.state_dict(),
                    'optimizer' : self.optimizer.state_dict(),
                   }, 'last_brain.pth')
    
    def load(self):
        if os.path.isfile('last_brain.pth'):
            print("=> loading checkpoint... ")
            checkpoint = torch.load('last_brain.pth')
            self.model.load_state_dict(checkpoint['state_dict'])
            self.optimizer.load_state_dict(checkpoint['optimizer'])
            print("done !")
        else:
            print("no checkpoint found...")
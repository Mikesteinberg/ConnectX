def my_agent(observation, configuration):
    from random import choice
    return choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    observation.board = list(map(lambda x: x if x != 2 else -1, observation.board))
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    observation.board = list(map(lambda x: x if x != 2 else -1, observation.board))
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    observation.board = list(map(lambda x: x if x != 2 else -1, observation.board))
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    observation.board = list(map(lambda x: x if x != 2 else -1, observation.board))
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    observation.board = list(map(lambda x: x if x != 2 else -1, observation.board))
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    observation.board = list(map(lambda x: x if x != 2 else -1, observation.board))
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    observation.board = list(map(lambda x: x if x != 2 else -1, observation.board))
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    reward_windows.append(np.mean(brain.reward_window))
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    reward_windows.append(np.mean(brain.reward_window))
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    reward_windows.append(np.mean(brain.reward_window))
    selection = action.item()
    return selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
def my_agent(observation, configuration):
    import time
    total_start = time.time()
    game.make_opponent_move(observation.board)
    print("***", game.current_state, "***")
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    reward_windows.append(np.mean(brain.reward_window))
    selection = action.item()
    selection = selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
    win_loss = game.check_for_win_or_loss()
    print(win_loss)
    chosen_move = None
    if win_loss[0] == 1:
        chosen_move = win_loss[1]
        right_move_picked = False
        print(f"TOTAL: {time.time() - total_start}")
        #print(chosen_move)
        return chosen_move
    elif win_loss[0] == -1:
        right_move_picked = True
        print(f"TOTAL: {time.time() - total_start}")
        #print(selection)
        return selection
    else:
        print("Else branch envoked")
        chosen_move = game.verify_move(selection)
        right_move_picked = True if selection == chosen_move else False
        print(f"TOTAL: {time.time() - total_start}")
        print(chosen_move)
        return chosen_move
def my_agent(observation, configuration):
    import time
    total_start = time.time()
    if observation.mark == 1:
        game.make_opponent_move(observation.board, 2)
        print("player 1")
    else:
        game.make_opponent_move(observation.board, 1)
        print("Player 2")
    #print("***", game.current_state, "***")
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    reward_windows.append(np.mean(brain.reward_window))
    selection = action.item()
    selection = selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
    win_loss = game.check_for_win_or_loss()
    #print(win_loss)
    chosen_move = None
    if win_loss[0] == 1:
        chosen_move = win_loss[1]
        right_move_picked = False
        #print(f"TOTAL: {time.time() - total_start}")
        #print(chosen_move)
        return chosen_move
    elif win_loss[0] == -1:
        right_move_picked = True
        #print(f"TOTAL: {time.time() - total_start}")
        #print(selection)
        return selection
    else:
        #print("Else branch envoked")
        chosen_move = game.verify_move(selection)
        right_move_picked = True if selection == chosen_move else False
        #print(f"TOTAL: {time.time() - total_start}")
        #print(chosen_move)
        return chosen_move
def my_agent(observation, configuration):
    import time
    total_start = time.time()
    if observation.mark == 1:
        game.make_opponent_move(observation.board, 2)
        print("player 1")
    else:
        game.make_opponent_move(observation.board, 1)
        print("Player 2")
    #print("***", game.current_state, "***")
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    reward_windows.append(np.mean(brain.reward_window))
    selection = action.item()
    selection = selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
    win_loss = game.check_for_win_or_loss()
    #print(win_loss)
    chosen_move = None
    if win_loss[0] == 1:
        chosen_move = win_loss[1]
        right_move_picked = False
        #print(f"TOTAL: {time.time() - total_start}")
        #print(chosen_move)
        return chosen_move
    elif win_loss[0] == -1:
        right_move_picked = True
        #print(f"TOTAL: {time.time() - total_start}")
        #print(selection)
        return selection
    else:
        #print("Else branch envoked")
        chosen_move = game.verify_move(selection)
        right_move_picked = True if selection == chosen_move else False
        #print(f"TOTAL: {time.time() - total_start}")
        #print(chosen_move)
        return chosen_move
def my_agent(observation, configuration):
    global game
    import time
    total_start = time.time()
    if observation.mark == 1:
        try:
            game.make_opponent_move(observation.board, 2)
            print("player 1")
        except:
            game = Game()
    else:
        game.make_opponent_move(observation.board, 1)
        print("Player 2")
    #print("***", game.current_state, "***")
    import random
    from random import choice
    action = brain.update(reward, observation.board)
    reward_windows.append(np.mean(brain.reward_window))
    selection = action.item()
    selection = selection if observation.board[selection] == 0 else choice([c for c in range(configuration.columns) if observation.board[c] == 0])
    win_loss = game.check_for_win_or_loss()
    #print(win_loss)
    chosen_move = None
    if win_loss[0] == 1:
        chosen_move = win_loss[1]
        right_move_picked = False
        #print(f"TOTAL: {time.time() - total_start}")
        #print(chosen_move)
        return chosen_move
    elif win_loss[0] == -1:
        right_move_picked = True
        #print(f"TOTAL: {time.time() - total_start}")
        #print(selection)
        return selection
    else:
        #print("Else branch envoked")
        chosen_move = game.verify_move(selection)
        right_move_picked = True if selection == chosen_move else False
        #print(f"TOTAL: {time.time() - total_start}")
        #print(chosen_move)
        return chosen_move

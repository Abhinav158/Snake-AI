#Import libraries 
import torch
import random
import numpy as np
from collections import deque
from game import SnakeGameAI, Direction, Point
from model import Linear_QNet, QTrainer
from helper import plot

# Store upto 100,000 elements in memory 
MAX_MEMORY = 100_000
# Batch Size of 1000
BATCH_SIZE = 1000
# Learning Rate of 0.001 
LR = 0.001

class Agent:

    def __init__(self):
        # Parameter to store number of games played 
        self.n_games = 0
        # Parameter to control the learning rate 
        self.epsilon = 0 
        # Discount rate gamma from the Bellman Equation
        self.gamma = 0.9 
        # Deque used for remembering values 
        # If we exceed memory, elements are popped from the left side 
        self.memory = deque(maxlen=MAX_MEMORY) 
        # Instance of the model 
        # Here, we have 11 possible states which serve as the input layer nodes
        # There are 3 output layer nodes since they determine the action given like [0,0,1]
        # Hidden layer is given as 256
        self.model = Linear_QNet(11, 256, 3)
        # The trainer gets the model, learning rate along with the gamma value 
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)


    def get_state(self, game):
        # Head of the snake is the first element of the list 
        head = game.snake[0]
        point_l = Point(head.x - 20, head.y)
        point_r = Point(head.x + 20, head.y)
        point_u = Point(head.x, head.y - 20)
        point_d = Point(head.x, head.y + 20)

        # Note: We use 20 since that is the value we have given for Block Size 
        
        dir_l = game.direction == Direction.LEFT
        dir_r = game.direction == Direction.RIGHT
        dir_u = game.direction == Direction.UP
        dir_d = game.direction == Direction.DOWN

        # Implement the 11 states we have available: 

        state = [
            # Danger straight
            (dir_r and game.is_collision(point_r)) or 
            (dir_l and game.is_collision(point_l)) or 
            (dir_u and game.is_collision(point_u)) or 
            (dir_d and game.is_collision(point_d)),

            # Danger right
            (dir_u and game.is_collision(point_r)) or 
            (dir_d and game.is_collision(point_l)) or 
            (dir_l and game.is_collision(point_u)) or 
            (dir_r and game.is_collision(point_d)),

            # Danger left
            (dir_d and game.is_collision(point_r)) or 
            (dir_u and game.is_collision(point_l)) or 
            (dir_r and game.is_collision(point_u)) or 
            (dir_l and game.is_collision(point_d)),
            
            # Movement 
            dir_l,
            dir_r,
            dir_u,
            dir_d,
            
            # Food location 
            game.food.x < game.head.x,  # food left
            game.food.x > game.head.x,  # food right
            game.food.y < game.head.y,  # food up
            game.food.y > game.head.y  # food down
            ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, done):
        # Here we want to remember these states by storing in memory 
        self.memory.append((state, action, reward, next_state, done)) 
        # Stores one tuple

    def train_long_memory(self): # Reminder: Batch Size = 1000
        # First check if we have 1000 samples in memory 
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
            # This returns a list of tuples  
        else: # If we do not have 1000 samples yet 
            mini_sample = self.memory

        # Extract from mini sample and put all states, actions, rewards, etc. together
        # This can be achieved using the built in zip function 
        states, actions, rewards, next_states, dones = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, dones)


    def train_short_memory(self, state, action, reward, next_state, done):
        self.trainer.train_step(state, action, reward, next_state, done)

    def get_action(self, state):

        # Initially perform random moves - Exploration of the environment         
        # As the model gets better, we shift to Exploitation

        # As we play more games, the epsilon value must decrease 
        self.epsilon = 80 - self.n_games
        final_move = [0,0,0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0, 2) # Choose radnomly from {0,1,2}
            final_move[move] = 1

        # Here, we move based on our model - so we get a prediction 
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1

        return final_move


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()
    while True:
        # get old state
        state_old = agent.get_state(game)

        # get move
        final_move = agent.get_action(state_old)

        # perform move and get new state
        reward, done, score = game.play_step(final_move)
        state_new = agent.get_state(game)

        # train short memory
        agent.train_short_memory(state_old, final_move, reward, state_new, done)

        # remember
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            # train long memory, plot result
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()

            print('Game: ', agent.n_games, 'Score: ', score, 'Record: ', record)

            # Add in the current store to the list 
            plot_scores.append(score)
            # Now calculate the mean score 
            total_score += score
            mean_score = total_score / agent.n_games
            # Append this to the mean_score list 
            plot_mean_scores.append(mean_score)
            # Plot
            plot(plot_scores, plot_mean_scores)


if __name__ == '__main__':
    train()
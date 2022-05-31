# import necessary libraries 
import pygame
import random
import numpy as np 
from enum import Enum
from collections import namedtuple


pygame.init()
font = pygame.font.Font('arial.ttf', 25)
#font = pygame.font.SysFont('arial', 25)

#Associate all directions with a number 
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')

# Colors using RGB values 
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

# Game block size and speed of the agent 
BLOCK_SIZE = 20
SPEED = 50

class SnakeGameAI:
    
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.reset()
        
        
    def reset(self):
        # set the initial game state where agent starts moving right upon starting
        self.direction = Direction.RIGHT
        
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        # Upon reset, set score to 0 and remove the previous food item 
        self.score = 0
        self.food = None

        # Now, initialise the board again along with number of frame iterations
        self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        #Random placement of food on the grid with each progressive level
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()
        
    def play_step(self, action):
        self.frame_iteration += 1
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
           
        
        self._move(action) # Update the head of the snake 
        self.snake.insert(0, self.head)
        
        # If collision occurs, game is over so set the corresponding variable to True
        reward = 0
        game_over = False
        if self.is_collision() or self.frame_iteration > 100*len(self.snake):
            game_over = True
            # Rewarded -10 for collisions 
            reward = -10
            return reward, game_over, self.score
            
        # If snake eats the randomly placed food, increment score and get +10 reward
        if self.head == self.food:            
            self.score += 1
            reward = 10
            self._place_food()
        else:
            self.snake.pop()
        
        #Update UI/Clock 
        self._update_ui()
        self.clock.tick(SPEED)
        
        return reward, game_over, self.score
    
    def is_collision(self, pt=None):
        if pt is None: 
            pt = self.head
        # Boundary hit 
        if pt.x > self.w - BLOCK_SIZE or pt.x < 0 or pt.y > self.h - BLOCK_SIZE or pt.y < 0:
            return True
        # Snake hits itself 
        if pt in self.snake[1:]:
            return True
        
        return False
        
    def _update_ui(self):
        self.display.fill(BLACK)
        
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
            
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
        
    def _move(self, action):

        # Actions possible : [straight, right, left]
        clock_wise = [Direction.RIGHT, Direction.DOWN, Direction.LEFT, Direction.UP]
        idx = clock_wise.index(self.direction)

        if np.array_equal(action, [1,0,0]):
            new_dir = clock_wise[idx] # No change in direction 
        elif np.array_equal(action, [0,1,0]):
            next_idx = (idx+1) % 4 # Right turn from current position
            new_dir = clock_wise[next_idx]
        else: # [0,0,1]
            next_idx = (idx-1) % 4 # Left turn frlom current position 
            new_dir = clock_wise[next_idx]

        self.direction = new_dir

        #Now update the co- ordinates based on the direction 
        x = self.head.x
        y = self.head.y
        if self.direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif self.direction == Direction.UP:
            y -= BLOCK_SIZE

        # Update the head    
        self.head = Point(x, y)
            


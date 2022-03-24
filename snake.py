from enum import Enum
from obstacle import*
'''
Creating Snake Class for:-
Keeping track of where the snake is.
Keeping track of the length of the snake.
Allowing the snake to grow.
Checking for collisions with the window boundaries.
Checking if the snake has crossed over ('bitten') itself
Keeping track of the direction the snake is moving in.
'''

class Direction(Enum):

  ### The number value ordering doesn't matter but shouldn't use duplicates
  UP = 4
  DOWN = 1
  LEFT = 2
  RIGHT = 3

class Snake:
  
  length = None
  direction = None
  body = None
  block_size = None
  color = (0, 0, 255)
  bounds = None

  def __init__(self, block_size, bounds):
    self.block_size = block_size
    self.bounds = bounds
    self.respawn()

  ## snake respawn and moves right 
  def respawn(self):
    self.length = 3
    self.body = [(150,140), (150,150), (150,160)]
    self.direction = Direction.RIGHT
  
  ## function to draw snake body, drawing each block using pygame.draw 
  def draw(self, game, window):
    for segment in self.body:
      game.draw.rect(window, self.color, (segment[0], segment[1], self.block_size, self.block_size))

  ## function to move snake in directions - up, down, left, right    
  def move(self):
    curr_head = self.body[-1]
    if self.direction == Direction.DOWN:
      next_head = (curr_head[0], curr_head[1] + self.block_size)
      self.body.append(next_head)
    elif self.direction == Direction.UP:
      next_head = (curr_head[0], curr_head[1] - self.block_size)
      self.body.append(next_head)
    elif self.direction == Direction.RIGHT:
      next_head = (curr_head[0] + self.block_size, curr_head[1])
      self.body.append(next_head)
    elif self.direction == Direction.LEFT:
      next_head = (curr_head[0] - self.block_size, curr_head[1])
      self.body.append(next_head)

    if self.length < len(self.body):
      self.body.pop(0)

   ## function to steer/direct snake 
  def steer(self, direction):
    if self.direction == Direction.DOWN and direction != Direction.UP:
      self.direction = direction
    elif self.direction == Direction.UP and direction != Direction.DOWN:
      self.direction = direction
    elif self.direction == Direction.LEFT and direction != Direction.RIGHT:
      self.direction = direction
    elif self.direction == Direction.RIGHT and direction != Direction.LEFT:
      self.direction = direction
  
  ## when eats, increases snake length
  def eat(self):
    self.length += 1
  
  ## if food cordinates matches the snake head cordinates, 
  ## eats food
  def check_for_eat(self, food, wall):
    head = self.body[-1]
    if head[0] == food.x and head[1] == food.y:
      self.eat()
      food.respawn(wall)
    
    ## if snake head cordinate matches body or tail, collision occurs
  def check_tail_collision(self):
    head = self.body[-1]
    has_eaten_tail = False

    for i in range(len(self.body)-1):
      segment = self.body[i]
      
      if segment[0] == head[0] and segment[1] == head[1]:
        has_eaten_tail = True

    return has_eaten_tail
  
  ## checking wall collision
  ## if snake head blocks matches any wall cordinates, collision occurs
  def check_wall_collision(self, wall):
    head = self.body[-1]
    has_hit_wall = False

    for i in range(len(wall.wall_line)):
      block = wall.wall_line[i]

      if block[0] == head[0] and block[1] == head[1]:
        has_hit_wall = True
    
    return has_hit_wall

  def check_bounds(self):
    head = self.body[-1]

    if head[0] >= self.bounds[0]:
      return True
    if head[1] >= self.bounds[1]:
      return True
    if head[0] < 0:
      return True
    if head[1] < 0:
      return True

    return False

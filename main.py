#importing classes and pygame
import pygame
from snake import *
from food import Food
from obstacle import Wall

'''
Initialize pygame modules and set bounds as screen width and height. Using display.set_mode() to display screen and set_caption to set screen title
'''
pygame.init()
bounds = (300, 300)

window = pygame.display.set_mode(bounds)

pygame.display.set_caption("Snake")

block_size = 10

# instantiating object for each classes
snake = Snake(block_size, bounds)
food = Food(block_size, bounds)
wall = Wall(block_size)
font = pygame.font.SysFont("comicsans", 60, True)

### game's main loop ###
run = True
while run:
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      
  ## pygame.key for keyboard inputs
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
    snake.steer(Direction.LEFT)
  elif keys[pygame.K_RIGHT]:
    snake.steer(Direction.RIGHT)
  elif keys[pygame.K_UP]:
    snake.steer(Direction.UP)
  elif keys[pygame.K_DOWN]:
    snake.steer(Direction.DOWN)

  snake.move()
  snake.check_for_eat(food,wall)

  ## checks collisions
  if snake.check_bounds() == True or snake.check_tail_collision() == True or snake.check_wall_collision(wall) == True:
    text = font.render("Game Over", True, (255, 0, 255))
    window.blit(text, (20, 120))
    pygame.display.update()
    pygame.time.delay(1000)
    snake.respawn()
    food.respawn(wall)
      
  #after quit, fill screen with blank to draw new snake
  window.fill((255,255,255))
  snake.draw(pygame, window)
  food.draw(pygame, window)
  wall.draw(pygame, window)
  pygame.display.update() #updates full display surface

  
  

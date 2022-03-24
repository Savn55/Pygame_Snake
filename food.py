import random
from obstacle import*

class Food:
  
  block_size = None
  color = (0, 255, 0)
  bounds = None
  x = 10
  y = 10

  def __init__(self, block_size, bounds):
    self.block_size = block_size 
    self.bounds = bounds

  def draw(self, game, window):
    appl = game.image.load("apple.png") # loads apple img from directory
    window.blit(appl, (self.x, self.y)) # blit displays the img to window

  ## Food appears at random coordinates  
  def random_cordinates(self):
    cordinate_x = self.bounds[0]/self.block_size # 300/10 = 30 blocks in x axis
    cordinate_y = self.bounds[1]/self.block_size # 30 blocks in y axis

    self.x = random.randint(0, cordinate_x -1) * self.block_size # mltplys by 10(food to fall within block size)
    self.y = random.randint(0, cordinate_y -1) * self.block_size
    return (self.x,self.y) 

  def respawn(self, wall):
    r = self.random_cordinates()
    # if food spawn inside wall_line list, call random_cordinates
    #if again spawn inside wall, need additional logic to deal with that, tried recurrsion but depth reaches easily
    while r in wall.wall_line:
      self.random_cordinates()
      
      

  

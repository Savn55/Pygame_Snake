
class Wall:

  #Creating the wall manually encoding cordinates 
  wall_line = [(120,140),(120,130),(120,120),(120,110),(120,100),(110,100),(100,100),
              (90,100),(80,100),(70,100),(70,90),(70,80),(70,70),(200,230),(200,240),(200,250),(190,250),
              (180,250),(170,250),(210,230),(210,220),(210,210),(210,200),(220,200),(230,200),(240,200),(250,200)]
  
  block_size = None #basically not required, just maintaining uniformity
  color = (0, 200, 200)

  def __init__(self, block_size):
    self.block_size = block_size

  def draw(self, game, window):
    for block in self.wall_line:
      # draws blocks for each tuple in the wall_line list
      game.draw.rect(window, self.color, (block[0], block[1], self.block_size, self.block_size))

      

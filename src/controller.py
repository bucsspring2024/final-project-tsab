import pygame
import sys
from player import Player
from ball import Ball
class Controller:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800, 600))
    self.clock=pygame.time.Clock()
    self.background=pygame.image.load('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/gui.jpg') 
    self.player1=Player('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/player1.jpg', (100,250))
    self.player2=Player('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/player2.jpg', (650,250))
    self.ball=Ball('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/ball.jpg', (400, 300))
    self.state='menu'
    self.running=True
  
    
  def mainloop(self):
    while self.running:
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          self.running=False
      if self.state=='menu':
        self.menuloop()
      elif self.state=='game':
        self.gameloop()
      elif self.state=='gameover':
        self.gameoverloop()
      else:
        self.running= False
      self.clock.tick(60)

  def menuloop(self):
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        self.running=False
    if pygame.key.get_pressed()[pygame.K_SPACE]:
      self.state='game'
    self.screen.fill((0,0,0))
    pygame.display.flip()
      
  def gameloop(self):
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        self.running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.player1.move(dy=-5)
    if keys[pygame.K_s]:
      self.player1.move(dy=5)
    if keys[pygame.K_UP]:
      self.player2.move(dy=-5)
    if keys[pygame.K_DOWN]:
      self.player2.move(dy=5)
    self.screen.fill((0,0,0))
    self.player1.draw(self.screen)
    self.player2.draw(self.screen)
    self.ball.draw(self.screen)
    pygame.display.flip()
  def gameoverloop(self):
    for event in pygame.event.get():
      if event.type== pygame.QUIT:
        self.running=False
    self.screen.fill((30,30,30))
    pygame.display.flip()
if __name__ == "__main__":
    ctrl = Controller()
    ctrl.mainloop()
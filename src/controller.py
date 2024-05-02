import pygame
import sys
from player import Player
from ball import Ball
from goal import Goal
class Controller:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800, 600))
    self.clock=pygame.time.Clock()
    self.background=pygame.image.load('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/gui.jpg') 
    self.ball=Ball('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/ball.jpg', (400, 300))
    self.player1=Player('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/player1.jpg', (100,250))
    self.player2=Player('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/player2.jpg', (700,250))
    self.goal1=Goal('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/goal1.jpg'(0,250))
    self.goal2=Goal('C:/Users/tarif/Downloads/final-project-tsab/final-project-tsab/assets/goal2.jpg', (800,250))
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
    font=pygame.font.Font(None,36)
    text=font.render('Press SPACE to start', True, (255,255,255))
    text_rect=text.get_rect(center=(400,300))
    self.screen.blit(text,text_rect)
    pygame.display.flip()
  def check_collisions(self):
      if self.player1.rect.colliderect(self.ball.rect):
        self.resolve_ball_collision(self.player1)
      if self.player2.rect.colliderect(self.ball.rect):
        self.resolve_ball_collision(self.player2)
  def resolve_ball_collision(self,player):
    """Changes the ball's direcion based on the player collision."""
    impact_velocity=[5,-5]    
    self.ball.activate(impact_velocity)
  def gameloop(self):
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        self.running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.player1.move(dy=-5)
    if keys[pygame.K_s]:
      self.player1.move(dy=5)
    if keys[pygame.K_a]:
      self.player1.move(dx=-5)
    if keys[pygame.K_d]:
      self.player1.move(dx=5)
    if keys[pygame.K_UP]:
      self.player2.move(dy=-5)
    if keys[pygame.K_DOWN]:
      self.player2.move(dy=5)
    if keys[pygame.K_RIGHT]:
      self.player2.move(dx=5)
    if keys[pygame.K_LEFT]:
      self.player2.move(dx=-5)
    self.ball.move()
    self.check_collisions()
    self.screen.fill((0,0,0))
    self.screen.blit(self.background,(0,0))
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
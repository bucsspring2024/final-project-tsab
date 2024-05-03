import pygame
import sys
from .player import Player
from .ball import Ball
from .goal import Goal
class Controller:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((800, 800))
    self.clock=pygame.time.Clock()
    self.background=pygame.image.load('assets/gui.jpg') 
    self.ball=Ball('assets/ball.jpg', (400, 300))
    self.player1=Player('assets/player1.jpg', (100,250))
    self.player2=Player('assets/player2.jpg', (650,250))
    self.player_names={
      self.player1:"Manblue",
      self.player2:"Manred"
    }
    self.scores={self.player1:0,self.player2:0}
    self.goal1=Goal('assets/goal1.jpg',(0,250))
    self.goal2=Goal('assets/goal2.jpg', (730,250))
    self.state='menu'
    self.running=True
    self.scores={self.player1:0, self.player2:0}
    self.game_time= 120
    self.timeout=0 
    self.button_color=(0,255,0)
    self.button_hover_color=(0,0,300)
    self.button_rect=pygame.Rect(300,500,200,50)
    self.button_text="Menu"
  def mainloop(self):
    start_ticks=pygame.time.get_ticks()
    while self.running:
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          self.running=False
      if self.state=='menu':
        self.menuloop()
      elif self.state=='menu2':
        self.menuloop2()
      elif self.state=='game':
        self.gameloop()
      elif self.state=='gameover':
        self.gameoverloop()
      else:
        self.running= False
      current_ticks=pygame.time.get_ticks()
      if (current_ticks - start_ticks)>= 1000:
          self.game_time -=1
          start_ticks =current_ticks

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
    

  def reset_game(self):
    self.player1.rect.topleft=(100,250)
    self.player2.rect.topleft=(650,250)
    self.ball.rect.center=(400,300)
    

  def check_collisions(self):
      if self.player1.rect.colliderect(self.ball.rect):
        self.resolve_ball_collision(self.player1)
      if self.player2.rect.colliderect(self.ball.rect):
        self.resolve_ball_collision(self.player2)
      if self.goal1.rect.colliderect(self.ball.rect):
        self.scores[self.player2]+= 1
        self.reset_game()
      elif self.goal2.rect.colliderect(self.ball.rect):
        self.scores[self.player1]+=1
        self.reset_game()
      
  
  def resolve_ball_collision(self,player):
    print("Collision detected")
    """Changes the ball's direcion based on the player collision."""
    x_diff=self.ball.rect.centerx - player.rect.centerx
    y_diff= self.ball.rect.centery - player.rect.centery
    print("Differences calculated: x_diff =", x_diff, ", y_diff =", y_diff)
    velocity_magnitude= 4
    print("Velocity magnitude set")
    if x_diff>0:
      self.ball.velocity[0]=velocity_magnitude
    else:
      self.ball.velocity[0]= -velocity_magnitude
    if y_diff>0:
       self.ball.velocity[1]=velocity_magnitude
    else:
      self.ball.velocity[1]= -velocity_magnitude
    print("Velocity assigned:", self.ball.velocity)
    self.ball.activate(self.ball.velocity)
    print("Ball activated")

  def update_timer(self):
    if self.clock.tick(60)==60:
       self.game_time-=1
  

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
    self.update_timer()
    self.update_display()
    if self.game_time<=0:
      self.state='gameover'
 
  def update_display(self):
    self.screen.fill((0,0,0))
    self.screen.blit(self.background,(0,0))
    self.draw_scoreboard()
    self.player1.draw(self.screen)
    self.player2.draw(self.screen)
    self.goal1.draw(self.screen)
    self.goal2.draw(self.screen)
    self.ball.draw(self.screen)
    pygame.display.flip()
  
  def draw_scoreboard(self):
    font=pygame.font.Font(None, 50)
    score_text = f'{self.player_names[self.player1]}:{self.scores[self.player1]} | {self.player_names[self.player2]}:{self.scores[self.player2]}'
    timer_text=f'Time Left:{self.game_time}'
    score_surface= font.render(score_text, True, (255,255,255))
    timer_surface = font.render(timer_text, True,(200,200,200))
    self.screen.blit(score_surface,(250,760))
    self.screen.blit(timer_surface, (250, 670))
 
  def draw_button(self, text, rect, color, action=None):
    mouse=pygame.mouse.get.pos()
    click=pygame.mouse.get_pressed()
    if rect.collidepoint(mouse):
      pygame.draw.rect(self.screen, self.button_hover_color,rect)
      if click[0]==1 and action is not None:
        action()
    else:
      pygame.draw.rect(self.screen, color, rect)
    text_surf=pygame.font.Font(None, 36).render(text, True, (255, 255, 255))
    text_rect= text_surf.get_rect(center=rect.center)
    self.screen.blit(text_surf, text_rect)

  def gameoverloop(self):
    while self.state=='gameover':
      for event in pygame.event.get():
          if event.type== pygame.QUIT: 
            self.running=False
            return           
      self.screen.fill((0,0,0))
      font=pygame.font.Font(None,72)
      game_over_text=font.render("Game Over", True, (0,0,255))
      game_over_rect=game_over_text.get_rect(center=(400,350))
      self.screen.blit(game_over_text, game_over_rect)
      score_font=pygame.font.Font(None, 48)
      score_text = score_font.render(f'Final Score - {self.player_names[self.player1]}: {self.scores[self.player1]} | {self.player_names[self.player2]}: {self.scores[self.player2]}', True, (255, 255, 255))
      score_rect=score_text.get_rect(center=(400,450))
      self.screen.blit(score_text, score_rect)
      self.draw_button(self.button_text, self.button_rect, self.button_color, self.restart_game)
    pygame.display.flip()
    self.clock.tick(30)

  def restart_game(self):
    self.player1.rect.topleft=(100,250)
    self.player2.rect.topleft=(650,250)
    self.ball.rect.center=(400,300)
    self.scores= {self.player1: 0, self.player2:0}
    self.game_time=120
    self.state='menu'

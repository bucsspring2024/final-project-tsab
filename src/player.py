import pygame
class Player:
    def __init__(self, image_path,position):
        self.image=pygame.image.load(image_path)
        self.rect=self.image.get_rect(topleft=position)
    def move(self, dx=0, dy=0):
        self.rect.x +=dx
        self.rect.y += dy
    def draw(self,surface):
        surface.blit(self.image,self.rect)
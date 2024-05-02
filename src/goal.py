import pygame
class Goal:
    def __init__(self, image_path,position):
        self.image=pygame.image.load(image_path)
        self.rect=self.image.get_rect(topleft=position)
    def draw(self,surface):
        surface.blit(self.image,self.rect)
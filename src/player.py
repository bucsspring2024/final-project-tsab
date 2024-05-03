import pygame
class Player:
    def __init__(self, image_path,position):
        self.image=pygame.image.load(image_path)
        self.rect=self.image.get_rect(topleft=position)

    def move(self, dx=0, dy=0):
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy
        screen_width, screen_height = 800, 600
        if 0 <= new_x <= screen_width - self.rect.width:
            self.rect.x = new_x
        if 0 <= new_y <= screen_height - self.rect.height:
            self.rect.y = new_y
    def draw(self,surface):
        surface.blit(self.image,self.rect)
        
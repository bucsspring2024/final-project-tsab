import pygame
class Ball:
    def __init__(self, image_path, position):
        self.image=pygame.image.load(image_path)
        self.rect=self.image.get_rect(center=position)
        self.velocity=[0,0]
        self.is_active=False
    def activate(self, initial_velocity):
        self.velocity=initial_velocity
        self.is_active=True
    def move(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if self.rect.left<=0 or self.rect.right>=800:
            self.velocity[0]=-self.velocity[0]
        if self.rect.top<=0 or self.rect.bottom>=600:
             self.velocity[1]=-self.velocity[1]
    def draw(self,surface):
        surface.blit(self.image,self.rect)

import pygame

class Brick:
    def __init__(self, pos x, pos y, image path):
    self.__image = pygame.image.load(image_path)
    self.__rect = self.image.get_rect()
    self.__rect.move_ip(pos_x, pos y)

@property
def rect(self):
    
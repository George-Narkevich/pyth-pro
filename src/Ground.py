import pygame

class Ground(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.image_ground = pygame.image.load('data/ground.png').convert() #загружаем изображение земли
        self.image_ground = pygame.transform.scale2x(self.image_ground) #зум чтобы красиво

        self.floor_x_pos = 0 #начальная горизонтальная позиция земли

    def draw_ground(self):
        self.screen.blit(self.image_ground, (self.floor_x_pos, 900)) #рисуем первое изображение земли
        self.screen.blit(self.image_ground, (self.floor_x_pos + 576, 900)) #второе
        self.floor_x_pos -= 2 #создаем эффект движения земли влево (птица, соответственно, вправо)
        if self.floor_x_pos <= -576: #нужно для иллюзии бесконечной ленты земли
            self.floor_x_pos = 0

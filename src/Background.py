import pygame
import random


class Background(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__() #конструктор родительского класса
        self.screen = screen

        self.image_day = pygame.image.load('data/background-day.png').convert() #подгружаем фоны
        self.image_night = pygame.image.load('data/background-night.png').convert()

        self.image_day = pygame.transform.scale2x(self.image_day) #зумим
        self.image_night = pygame.transform.scale2x(self.image_night)

        self.number = random.randint(0, 1)#будем выбирать рандомный фон

    def back(self): #метод непосредственно создает фон в зависимости от рандомно выбранного числа для фона
        if self.number == 0:
            self.screen.blit(self.image_day, (0, 0))
        if self.number == 1:
            self.screen.blit(self.image_night, (0, 0))

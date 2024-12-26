import pygame, random #random будет выбирать цвет птицы


class Bird(pygame.sprite.Sprite): #наследуем и получаем возможность быть графическим объектом
    def __init__(self, *screen):
        super().__init__()
        self.image = pygame.image.load('data/bluebird-upflap.png') #загружаем изображение птицы (в начале синяя с поднятыми крыльями)
        self.image = pygame.transform.scale2x(self.image) #увеличиваем размер птицы
        self.screen = screen[0] #поверхность экрана
        self.rect = self.image.get_rect() #для определения положения и столкновений делаем вокруг птицы прямоугольную область
        self.rect.x = 100
        self.rect.y = 100 #начальные координаты
        self.screen.blit(self.image, (self.rect.x, self.rect.y)) #рисуем птицу на экране
        self.count = 0
        self.check_score = True
        self.number = random.randint(0, 2) #рандомный цвет птицы
        self.bird_rect = self.image.get_rect(center=(self.rect.x, self.rect.y)) #так отрисовываем повернутую птицу
        self.move_bird = 0 #угол

    def spin_bird(self):

        new_bird = pygame.transform.rotozoom(self.image, self.move_bird * 3, 1) #поворачиваем и масштабируем
        return new_bird

    def update(self, *args):
        self.bird_rect = self.image.get_rect(center=(self.rect.x, self.rect.y)) #обновляем область
        if self.rect.y <= 30:
            self.rect.y += 7
        if self.rect.y >= 880: #проверяем нахождение в пределах границ экрана
            self.count = 1
            self.rect.y += 0
        else: #хотим, чтобы птица падала, когда никакая кнопка не нажата
            if args and args[0].type == pygame.KEYDOWN:
                if args[0].key == pygame.K_UP:
                    self.move_bird = 0
                    self.move_bird += 1.5
                    if self.number == 0:
                        self.image = pygame.image.load('data/bluebird-upflap.png')
                        self.image = pygame.transform.scale2x(self.image)
                        self.rect.y -= 10
                    elif self.number == 1:
                        self.image = pygame.image.load('data/redbird-upflap.png')
                        self.image = pygame.transform.scale2x(self.image)
                        self.rect.y -= 10
                    else:
                        self.image = pygame.image.load('data/yellowbird-upflap.png')
                        self.image = pygame.transform.scale2x(self.image)
                        self.rect.y -= 10

            else:
                if self.move_bird >= -25:
                    self.move_bird -= 0.7
                else:
                    self.move_bird -= 0
                if self.number == 0:
                        self.image = pygame.image.load('data/bluebird-downflap.png')
                        self.image = pygame.transform.scale2x(self.image)
                        self.rect.y += 7
                elif self.number == 1:
                        self.image = pygame.image.load('data/redbird-downflap.png')
                        self.image = pygame.transform.scale2x(self.image)
                        self.rect.y += 7
                else:
                        self.image = pygame.image.load('data/yellowbird-downflap.png')
                        self.image = pygame.transform.scale2x(self.image)
                        self.rect.y += 7
        self.screen.blit(self.spin_bird(), (self.rect.x, self.rect.y)) #рисуем повернутую птицу

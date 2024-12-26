import pygame


class GameOver(pygame.sprite.Sprite):
    def __init__(self, screen):#снова конструктор класса sprite
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('data/message.png') #картинка завершения игры
        self.image = pygame.transform.scale2x(self.image) #зум
        self.game_font = pygame.font.Font('data/FONT.TTF', 30)
        self.score = 0 #текущий счет
        self.vote = pygame.mixer.Sound('data/Game_Over.wav') #звук завершения игры
        self.score_max = 0 #максимальный счет
        self.check_game = False
    def update(self):
        self.screen.blit(self.image, (100, 256))#отображаем картинку завершения игры

    def game_over(self):
        self.vote.play() #воспроизводим звук

    def delete_image(self):
        self.screen.fill((255, 255, 255)) #заполняем экран

    def score_up(self): #метод отображения счета
        score_surface = self.game_font.render(f'Score: {int(self.score)}', True, (255, 255, 255))#текст с текущим счетом
        score_rect = score_surface.get_rect(center=(300, 70))#прямоугольная область вокруг текста со счетом, устанавливаем в центр
        high_score_surface = self.game_font.render(f'High Score: {int(self.score_max)}', True, (255, 255, 255)) #аналогично для макс счета
        high_score_rect = high_score_surface.get_rect(center=(120, 20))
        self.screen.blit(score_surface, score_rect)#отображение
        self.screen.blit(high_score_surface, high_score_rect)

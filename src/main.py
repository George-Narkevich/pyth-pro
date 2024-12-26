import pygame #подлючаем все требуемое + из других файлов
import random
from Background import Background
from Ground import Ground
from Bird import Bird
from GameOver import GameOver


def main():
    pygame.init() #инициируем все модули пайгейм

    def pipe_create(): #создаем верхную и нижнюю колонны случайной высоты
        pipe_pos = random.choice(pipe_height)
        down_pipe = pipe_surface.get_rect(midtop=(700, pipe_pos))
        up_pipe = pipe_surface.get_rect(midbottom=(700, pipe_pos - 300))
        return down_pipe, up_pipe

    def move_pipes(pipes): #двигам колонны
        for pipe in pipes:
            pipe.centerx -= 5
        vis_pipes = [pipe for pipe in pipes if pipe.right > -50]
        return vis_pipes

    def draw_pipes(pipes): #отрисовываем колонны
        for pipe in pipes:
            if pipe.bottom >= 1024:
                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)

    def delete_pipe(pipes): #колонна за пределами экрана --> убираем ее
        for pipe in pipes:
            if pipe.centerx == -600:
                pipes.remove(pipe)
        return pipes

    def collision(pipes): #проверяем, столкнулась ли птица с колонной
        for pipe in pipes:
            if bird.bird_rect.colliderect(pipe):
                bird.check_score = True
                return False
        return True

    def pipe_score_check(): #если прошла --> увеличиваем счет
            for pipe in pipe_list:
                if 98 < pipe.centerx < 102 and bird.check_score:
                        game_over.score += 1
                        game_over.score_up()
                        sound.play()
                        bird.check_score = False
                if game_over.score > game_over.score_max:
                    game_over.score_max = game_over.score
                if pipe.centerx < 0:
                    bird.check_score = True

    clock = pygame.time.Clock() #частота кадров
    WIDTH = 576
    HEIGHT = 1024
    SIZE = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(SIZE) #создаем окно игры
    sound = pygame.mixer.Sound('data/sfx_point.wav') #звук "+score"
    number_pipe = random.randint(0, 1) #случайный цвет колонн
    if number_pipe == 0:
        pipe_surface = pygame.image.load('data/pipe-green.png')
    else:
        pipe_surface = pygame.image.load('data/pipe-red.png')
    pipe_surface = pygame.transform.scale2x(pipe_surface)
    pipe_list = [] #список колонн
    pipe_height = [400, 600, 800] #возможные высоты
    create_pipe = pygame.USEREVENT
    pygame.time.set_timer(create_pipe, 1200) #генерируем новые колонны по истечении заданного времени
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    back = Background(screen) #объекты классов
    ground = Ground(screen)
    bird = Bird(screen)
    game_over = GameOver(screen)
    done = True #играем, пока сами не закроем окно
    while done:
        clock.tick(60) #макс частота кадров
        back.back()
        ground.draw_ground()

        game_over.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False

            if event.type == create_pipe:
                pipe_list.extend(pipe_create())

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: #для старта игры нажимаем вверх
                    game_over.check_game = True
        if game_over.check_game:
            game_over.delete_image()
            back.back()
            ground.draw_ground()
            pipe_list = move_pipes(pipe_list)
            pipe_list = delete_pipe(pipe_list)
            draw_pipes(pipe_list)
            bird.update(event)
            bird.spin_bird()
            game_over.check_game = collision(pipe_list)
            pipe_score_check()
            game_over.score_up()
        if bird.rect.y >= 880 or collision(pipe_list) is False:
            bird.rect.x = 100
            bird.rect.y = 100
            game_over.check_game = False
            bird.move_bird = 0
            pipe_list.clear()
            game_over.score_up()
            game_over.update()
            game_over.score_up()
            game_over.game_over()
        if not game_over.check_game:
            bird.move_bird = 0
            game_over.score = 0
            pipe_list.clear()
        pygame.display.flip()
        pygame.display.update()


if __name__ == "__main__":
    main()

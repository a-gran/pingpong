import pygame                                                           # Импортируем библиотеку pygame

class GameSprite(pygame.sprite.Sprite):                                  # Объявление класса-родителя для всех спрайтов
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):  # Конструктор с параметрами        
        super().__init__()                                               # Вызов конструктора класса-родителя        
        self.image = pygame.transform.scale(pygame.image.load(player_image), (width, height))  # Загрузка и масштабирование изображения
        self.speed = player_speed                                        # Установка скорости спрайта
        self.rect = self.image.get_rect()                                # Получение прямоугольника изображения
        self.rect.x = player_x                                           # Установка x-координаты спрайта
        self.rect.y = player_y                                           # Установка y-координаты спрайта

    def reset(self):                                                     # Метод для отрисовки спрайта
        window.blit(self.image, (self.rect.x, self.rect.y))              # Отрисовка изображения на экране

class Player(GameSprite):                                                # Объявление класса-наследника для игроков
    def __init__(self, player_image, player_x, player_y, player_speed, width, height, points):  # Конструктор с дополнительным параметром points
        super().__init__(player_image, player_x, player_y, player_speed, width, height)  # Вызов конструктора родителя
        self.points = points                                             # Установка начального количества очков

    def update_r(self):                                                  # Метод для управления правым игроком
        keys = pygame.key.get_pressed()                                  # Получение состояния всех клавиш
        if keys[pygame.K_UP] and self.rect.y > 5:                        # Если нажата стрелка вверх и не достигнут верхний край
            self.rect.y -= self.speed                                    # Перемещение вверх
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:        # Если нажата стрелка вниз и не достигнут нижний край
            self.rect.y += self.speed                                    # Перемещение вниз
            if self.rect.y > 550:                                        # Дополнительная проверка нижней границы
                self.rect.y = 550                                        # Установка максимального значения y

    def update_l(self):                                                  # Метод для управления левым игроком
        keys = pygame.key.get_pressed()                                  # Получение состояния всех клавиш
        if keys[pygame.K_w] and self.rect.y > 5:                         # Если нажата клавиша W и не достигнут верхний край
            self.rect.y -= self.speed                                    # Перемещение вверх
        if keys[pygame.K_s] and self.rect.y < win_height - 80:           # Если нажата клавиша S и не достигнут нижний край
            self.rect.y += self.speed                                    # Перемещение вниз
            if self.rect.y > 550:                                        # Дополнительная проверка нижней границы
                self.rect.y = 550                                        # Установка максимального значения y

img_back = 'galaxy.png'                                                  # Путь к фоновому изображению
img_asteroid = 'asteroid.png'                                            # Путь к изображению мяча (астероида)
img_racket = 'racket.png'                                                # Путь к изображению ракетки

back = (200, 255, 255)                                                   # Цвет фона (background)
win_width = 1200                                                         # Ширина окна игры
win_height = 700                                                         # Высота окна игры
window = pygame.display.set_mode((win_width, win_height))                # Создание игрового окна
background = pygame.transform.scale(pygame.image.load(img_back), (win_width, win_height))  # Загрузка и масштабирование фона
#window.fill(back)                                                       # Закомментированная строка заливки окна цветом

pygame.font.init()                                                       # Инициализация модуля шрифтов
font1 = pygame.font.Font(None, 72)                                       # Создание шрифта для сообщений о проигрыше
font2 = pygame.font.Font(None, 36)                                       # Создание шрифта для отображения счета
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))                # Создание текста о проигрыше первого игрока
lose2 = font1.render('PLAYER 2 LOSE!', True, (180, 0, 0))                # Создание текста о проигрыше второго игрока

pygame.mixer.init()                                                      # Инициализация звукового модуля
pygame.mixer.music.load('space.ogg')                                     # Загрузка музыкального файла
pygame.mixer.music.play()                                                # Воспроизведение музыки

game = True                                                              # Флаг активности основного игрового цикла
finish = False                                                           # Флаг завершения игры
game_over = False                                                        # Флаг окончания игры (не используется)
clock = pygame.time.Clock()                                              # Создание таймера
FPS = 60                                                                 # Установка частоты кадров

racket1 = Player(img_racket, 30, 200, 4, 50, 150, 0)                     # Создание левого игрока
racket2 = Player(img_racket, 1120, 200, 4, 50, 150, 0)                   # Создание правого игрока
ball = GameSprite(img_asteroid, 200, 200, 4, 50, 50)                     # Создание мяча

speed_x = 4                                                              # Горизонтальная скорость мяча
speed_y = 4                                                              # Вертикальная скорость мяча

while game:                                                              # Основной игровой цикл
    for e in pygame.event.get():                                         # Обработка всех событий
        if e.type == pygame.QUIT:                                        # Если нажат крестик закрытия окна
            game = False                                                 # Завершение игры

    if finish != True:                                                   # Если игра не завершена
        score = font2.render("Счет: " + str(racket1.points) + ' : ' + str(racket2.points), 1, (255, 255, 255))  # Создание текста со счетом
        window.blit(score, (500, 20))                                    # Отображение счета на экране
        #window.fill(back)                                               # Закомментированная строка заливки окна цветом
        window.blit(background,(0,0))                                    # Отрисовка фонового изображения
        racket1.update_l()                                               # Обновление положения левого игрока
        racket2.update_r()                                               # Обновление положения правого игрока
        ball.rect.x += speed_x                                           # Изменение x-координаты мяча
        ball.rect.y += speed_y                                           # Изменение y-координаты мяча

        if pygame.sprite.collide_rect(racket1, ball) or pygame.sprite.collide_rect(racket2, ball):  # Если мяч столкнулся с ракеткой
            speed_x *= -1                                                # Изменение направления по горизонтали
            speed_y *= 1                                                 # Сохранение направления по вертикали

        if ball.rect.y > win_height-50 or ball.rect.y < 0:               # Если мяч достиг верхней или нижней границы
            speed_y *= -1                                                # Изменение направления по вертикали

        if ball.rect.x < 0:                                              # Если мяч вылетел за левую границу
            racket2.points += 1                                          # Начисление очка правому игроку
            if racket2.points > 5:                                       # Если правый игрок набрал больше 5 очков
                finish = True                                            # Завершение игры
                window.blit(lose1, (400, 300))                           # Отображение сообщения о проигрыше левого игрока
                #game_over = True                                        # Закомментированный флаг окончания игры

        if ball.rect.x > win_width:                                      # Если мяч вылетел за правую границу
            racket1.points += 1                                          # Начисление очка левому игроку
            if racket1.points > 5:                                       # Если левый игрок набрал больше 5 очков
                finish = True                                            # Завершение игры
                window.blit(lose2, (400, 300))                           # Отображение сообщения о проигрыше правого игрока
                #game_over = True                                        # Закомментированный флаг окончания игры

        racket1.reset()                                                  # Отрисовка левого игрока
        racket2.reset()                                                  # Отрисовка правого игрока
        ball.reset()                                                     # Отрисовка мяча

    pygame.display.update()                                              # Обновление экрана
    clock.tick(FPS)                                                      # Установка скорости игры
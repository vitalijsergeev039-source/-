import pygame
import math
import random
import os
#использую os, так как были проблемы с поиском файлов, на ноутбуке
#нашел этот совет в интернете
pygame.init()
script_dir = os.path.dirname(os.path.abspath(__file__))

#Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра: Пушка против птиц")

#Фон
background = pygame.image.load(os.path.join(script_dir, "1.jpg")).convert()  
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#Изображения
bird_image = pygame.image.load(os.path.join(script_dir, "2.png")).convert_alpha() 
bird_image = pygame.transform.scale(bird_image, (60, 45))

slingshot_image = pygame.image.load(os.path.join(script_dir, "3.png")).convert_alpha() 
slingshot_image = pygame.transform.scale(slingshot_image, (100, 100))

ball_image = pygame.image.load(os.path.join(script_dir, "4.png")).convert_alpha()  
ball_image = pygame.transform.scale(ball_image, (25, 25))
#Музыка и звуки
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(script_dir, "5.mp3"))  
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

hit_sound = pygame.mixer.Sound(os.path.join(script_dir, "6.mp3"))  
hit_sound.set_volume(0.7)

#Параметры физики
gravity = 0.4
power = 15
angle = 45
ball_radius = 10

#Начальные координаты рогатки
start_x, start_y = 120, HEIGHT - 100
on_ground = True
vx, vy = 0, 0
x, y = start_x, start_y

#Птицы
NUM_BIRDS = 5
birds = []
for i in range(NUM_BIRDS):
    bx = random.randint(WIDTH, WIDTH + 400)
    by = random.randint(50, 300)
    speed = random.uniform(2, 5)
    birds.append([bx, by, speed])

#Текст
font = pygame.font.Font(None, 28)

#Счёт
score = 0
paused = False

#Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                angle = min(angle + 5, 80)
            elif event.key == pygame.K_DOWN:
                angle = max(angle - 5, 10)
            elif event.key == pygame.K_w:
                power = min(power + 1, 30)
            elif event.key == pygame.K_s:
                power = max(power - 1, 5)
            elif event.key == pygame.K_SPACE and on_ground:
                rad = math.radians(angle)
                vx = power * math.cos(rad)
                vy = -power * math.sin(rad)
                on_ground = False
            elif event.key == pygame.K_p:
                paused = not paused
                if paused:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

    if not paused:
        #Движение птиц 
        for bird in birds:
            bird[0] -= bird[2]
            if bird[0] < -60:  # возвращаем птицу с другой стороны
                bird[0] = random.randint(WIDTH + 100, WIDTH + 400)
                bird[1] = random.randint(50, 300)
                bird[2] = random.uniform(2, 5)

        #Полёт шарика
        if not on_ground:
            vy += gravity
            x += vx
            y += vy

            # Столкновение с землёй
            if y + ball_radius >= HEIGHT - 30:
                y = HEIGHT - 30 - ball_radius
                vx = 0
                vy = 0
                on_ground = True
                x, y = start_x, start_y

        #Проверка попаданий
        ball_rect = pygame.Rect(x - ball_radius, y - ball_radius, ball_radius * 2, ball_radius * 2)
        for bird in birds:
            bird_rect = pygame.Rect(bird[0], bird[1], 60, 45)
            if ball_rect.colliderect(bird_rect):
                hit_sound.play()
                score += 1
                # Возрождение птицы
                bird[0] = random.randint(WIDTH + 100, WIDTH + 400)
                bird[1] = random.randint(50, 300)
                bird[2] = random.uniform(2, 5)
                # Сброс шарика
                x, y = start_x, start_y
                on_ground = True
                vx, vy = 0, 0
                break

    #Отрисовка
    screen.blit(background, (0, 0))
    screen.blit(slingshot_image, (start_x - 60, start_y - 70))

    #Траектория (если шарик не запущен)
    if on_ground and not paused:
        traj_points = []
        rad = math.radians(angle)
        temp_vx = power * math.cos(rad)
        temp_vy = -power * math.sin(rad)
        temp_x, temp_y = start_x, start_y
        for i in range(100):
            temp_vy += gravity
            temp_x += temp_vx
            temp_y += temp_vy
            if temp_y + ball_radius >= HEIGHT - 30:
                break
            traj_points.append((int(temp_x), int(temp_y)))
        if len(traj_points) > 1:
            pygame.draw.lines(screen, (50, 50, 50), False, traj_points, 2)

    #Птицы
    for bird in birds:
        screen.blit(bird_image, (bird[0], bird[1]))

    #Шарик
    screen.blit(ball_image, (int(x - ball_radius), int(y - ball_radius)))

    # --- Информация ---
    text_angle = font.render(f"Угол: {angle}°", True, (255, 255, 255))
    text_power = font.render(f"Сила: {power}", True, (255, 255, 255))
    text_score = font.render(f"Счёт: {score}", True, (255, 255, 0))
    screen.blit(text_angle, (10, 10))
    screen.blit(text_power, (10, 30))
    screen.blit(text_score, (10, 50))

    if paused:
        pause_text = font.render("ПАУЗА", True, (255, 0, 0))
        screen.blit(pause_text, (WIDTH // 2 - 40, HEIGHT // 2))

    pygame.display.flip()
    pygame.time.delay(20)

pygame.quit()


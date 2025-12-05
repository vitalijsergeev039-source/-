import pygame
import os
import random
import math

# Настройка pygame
pygame.init()
pygame.mixer.init()

BASE = os.path.dirname(os.path.abspath(__file__))

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Птицы и крысы")

def load_image(path, scale=None):
    if not os.path.isfile(path):
        raise SystemExit(f"Файл не найден: {path}")
    img = pygame.image.load(path).convert_alpha()   
    if scale:
        img = pygame.transform.scale(img, scale)
    return img

def load_sound(path):
    if not os.path.isfile(path):
        raise SystemExit(f"Файл не найден: {path}")
    return pygame.mixer.Sound(path)

def load_music(path):
    if not os.path.isfile(path):
        raise SystemExit(f"Файл не найден: {path}")
    pygame.mixer.music.load(path)

# Файлы
BG_FILE = os.path.join(BASE, "1.webp")
PLAYER_FILE = os.path.join(BASE, "2.png")  
BIRD_FILE = os.path.join(BASE, "3.png")
RAT_FILE = os.path.join(BASE, "4.png")     
STONE_FILE = os.path.join(BASE, "5.png")

MUSIC_FILE = os.path.join(BASE, "6.mp3")
HIT_SOUND_FILE = os.path.join(BASE, "7.mp3")
HURT_SOUND_FILE = os.path.join(BASE, "8.mp3")
LOSE_SOUND_FILE = os.path.join(BASE, "9.mp3")
WIN_SOUND_FILE = os.path.join(BASE, "10.mp3")

# Загрузка
bg_img_raw = pygame.image.load(BG_FILE).convert()    
bg_img = pygame.transform.scale(bg_img_raw, (WIDTH, HEIGHT))

player_img = load_image(PLAYER_FILE, scale=(90, 120))
bird_img = load_image(BIRD_FILE, scale=(70, 50))
rat_img = load_image(RAT_FILE, scale=(80, 50))
stone_img = load_image(STONE_FILE, scale=(22, 22))

hit_sound = load_sound(HIT_SOUND_FILE)
hurt_sound = load_sound(HURT_SOUND_FILE)
lose_sound = load_sound(LOSE_SOUND_FILE)
win_sound = load_sound(WIN_SOUND_FILE)

load_music(MUSIC_FILE)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 28)

player_world_x = WIDTH -700
player_y = HEIGHT - 120
player_vx = 0.0
player_vy = 0.0
player_speed = 6.0
jump_speed = -14.0
gravity = 0.7
facing_right = True

stones = []
birds = []
rats = []

score = 0
hits_taken = 0
max_hit = 3
win_score = 10

bird_spavn_interval = 10000
rat_spavn_interval = 1

last_bird_spawn = pygame.time.get_ticks()
last_rat_spawn = pygame.time.get_ticks()

throw_angle = 45
throw_power = 14

def spawn_bird():
    x = random.randint(WIDTH + 50, WIDTH + 400)
    y = random.randint(40, max(100, HEIGHT // 2))
    speed = random.uniform(2.0, 4.0)
    birds.append({'x': x, 'y': y, 'speed': speed})

def spawn_rat():
    if len(rats) < 1:
        x = random.randint(WIDTH + 50, WIDTH + 100)
        y = player_y + 60
        speed = random.uniform(3.0, 5.0)
        rats.append({'x': x, 'y': y, 'speed': speed})

for _ in range(3):
    spawn_bird()

def world_to_screen(wx):
    return int(WIDTH // 2 + (wx - player_world_x))

def rect_from(img, wx, wy):
    return pygame.Rect(world_to_screen(wx), int(wy), img.get_width(), img.get_height())

def relocate_rats_to_ground():
    for r in rats:
        r['y'] = player_y + 30

running = True
game_over = False
game_won = False
fullscreen = False

while running:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Изменение размера окна
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            
            bg_img = pygame.transform.scale(bg_img_raw, (WIDTH, HEIGHT))

            if player_y > player_y:
                player_y = player_y
                player_vy = 0.0

            relocate_rats_to_ground()

        if event.type == pygame.KEYDOWN:

            # Fullscreen
            if event.key == pygame.K_RETURN and (pygame.key.get_mods() & pygame.KMOD_ALT):
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

                WIDTH, HEIGHT = screen.get_size()
                player_y = HEIGHT - 120
                bg_img = pygame.transform.scale(bg_img_raw, (WIDTH, HEIGHT))
                relocate_rats_to_ground()

            # Restart
            if event.key == pygame.K_SPACE and (game_over or game_won):
                birds.clear()
                rats.clear()
                stones.clear()
                score = 0
                hits_taken = 0
                game_over = False
                game_won = False
                player_world_x = 200.0
                player_y = HEIGHT - 120
                for _ in range(3):
                    spawn_bird()
                pygame.mixer.music.play(-1)

            if not game_over and not game_won:

                # Прыжок
                if event.key == pygame.K_w and abs(player_y - player_y) < 1:
                    player_vy = jump_speed

                # Угол
                if event.key == pygame.K_UP:
                    throw_angle = min(80, throw_angle + 5)
                if event.key == pygame.K_DOWN:
                    throw_angle = max(10, throw_angle - 5)

                # Сила
                if event.key == pygame.K_RIGHT:
                    throw_power = min(30, throw_power + 1)
                if event.key == pygame.K_LEFT:
                    throw_power = max(5, throw_power - 1)

                # Бросок камня
                if event.key == pygame.K_j:
                    rad = math.radians(throw_angle)
                    vx = math.cos(rad) * throw_power
                    vy = -math.sin(rad) * throw_power
                    if not facing_right:
                        vx = -vx
                    stones.append({
                        'x': player_world_x,
                        'y': player_y + 20,
                        'vx': vx,
                        'vy': vy
                    })

    # Игровая логика
    if not game_over and not game_won:

        keys = pygame.key.get_pressed()
        player_vx = 0.0

        if keys[pygame.K_a]:
            player_vx = -player_speed
            facing_right = False
        if keys[pygame.K_d]:
            player_vx = player_speed
            facing_right = True

        player_world_x += player_vx

        player_vy += gravity
        player_y += player_vy
        if player_y >= HEIGHT - 120:
            player_y = HEIGHT - 120
            player_vy = 0.0

        now = pygame.time.get_ticks()

        if now - last_bird_spawn > bird_spavn_interval:
            spawn_bird()
            last_bird_spawn = now

        if now - last_rat_spawn > rat_spavn_interval:
            spawn_rat()
            last_rat_spawn = now

        for b in birds:
            b['x'] -= b['speed']
            if b['x'] < player_world_x - WIDTH:
                b['x'] = player_world_x + random.randint(WIDTH, WIDTH + 300)
                b['y'] = random.randint(40, max(100, HEIGHT // 2))

        for r in rats[:]:
            r['x'] -= r['speed']
            if r['x'] < player_world_x - WIDTH:
                rats.remove(r)

        for s in stones:
            s['vy'] += gravity * 0.8
            s['x'] += s['vx']
            s['y'] += s['vy']

        stones = [
            s for s in stones
            if -400 < s['y'] < HEIGHT + 400 and abs(s['x'] - player_world_x) < WIDTH * 2
        ]

        # Взаимодействие птицы и камня
        for s in stones[:]:
            s_rect = pygame.Rect(
                world_to_screen(s['x']), int(s['y']),
                stone_img.get_width(), stone_img.get_height()
            )
            for b in birds[:]:
                if s_rect.colliderect(rect_from(bird_img, b['x'], b['y'])):
                    hit_sound.play()
                    score += 1
                    birds.remove(b)
                    spawn_bird()
                    stones.remove(s)
                    break

        # Взаимодействие крысы и игрока
        player_rect = pygame.Rect(
            WIDTH // 2 - player_img.get_width() // 2,
            int(player_y),
            player_img.get_width(),
            player_img.get_height()
        )
        for r in rats[:]:
            if player_rect.colliderect(rect_from(rat_img, r['x'], r['y'])):
                hurt_sound.play()
                hits_taken += 1
                rats.remove(r)

        if score >= win_score:
            win_sound.play()
            pygame.mixer.music.stop()
            game_won = True

        if hits_taken >= max_hit:
            lose_sound.play()
            pygame.mixer.music.stop()
            game_over = True

    # Отрисовка
    bg_x = -int(player_world_x) % WIDTH
    screen.blit(bg_img, (bg_x, 0))
    screen.blit(bg_img, (bg_x - WIDTH, 0))

    for b in birds:
        screen.blit(bird_img, (world_to_screen(b['x']), b['y']))

    for r in rats:
        screen.blit(rat_img, (world_to_screen(r['x']), r['y']))

    for s in stones:
        screen.blit(stone_img, (world_to_screen(s['x']), int(s['y'])))

    px = WIDTH // 2 - player_img.get_width() // 2
    img = player_img if facing_right else pygame.transform.flip(player_img, True, False)
    screen.blit(img, (px, int(player_y)))

    screen.blit(FONT.render(f"Счёт: {score}", True, (255, 255, 0)), (10, 10))
    screen.blit(FONT.render(f"Удары: {hits_taken}/{max_hit}", True, (255, 100, 100)), (10, 40))
    screen.blit(FONT.render(f"Угол: {throw_angle}°", True, (255, 255, 255)), (10, 70))
    screen.blit(FONT.render(f"Сила: {throw_power}", True, (255, 255, 255)), (10, 90))

    if game_over:
        msg = pygame.font.Font(None, 70).render("ПОРАЖЕНИЕ!", True, (255, 50, 50))
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 40))

    if game_won:
        msg = pygame.font.Font(None, 70).render("ПОБЕДА!", True, (50, 255, 50))
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 40))

    pygame.display.flip()

pygame.quit()

import pygame
import math
import random
import os
from pygame import mixer

pygame.init()
mixer.init()

# Настройки экрана
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Солнечная система")
clock = pygame.time.Clock()
FPS = 60

cx = WIDTH // 2
cy = HEIGHT // 2

# Файлы
BASE_DIR = os.path.dirname(__file__)

SUN_IMAGE = os.path.join(BASE_DIR, "21.jpg")
MERCURY_IMAGE = os.path.join(BASE_DIR, "10.jpg")
VENUS_IMAGE   = os.path.join(BASE_DIR, "11.jpg")
EARTH_IMAGE   = os.path.join(BASE_DIR, "13.jpg")
MOON_IMAGE    = os.path.join(BASE_DIR, "20.jpg")
MARS_IMAGE    = os.path.join(BASE_DIR, "14.jpg")
JUPITER_IMAGE = os.path.join(BASE_DIR, "15.jpg")
SATURN_IMAGE  = os.path.join(BASE_DIR, "16.jpg")
URANUS_IMAGE  = os.path.join(BASE_DIR, "17.jpg")
NEPTUNE_IMAGE = os.path.join(BASE_DIR, "18.jpg")
PLUTO_IMAGE   = os.path.join(BASE_DIR, "19.jpg")
COMET_IMAGE   = os.path.join(BASE_DIR, "22.jpg")

MUSIC_FILE = os.path.join(BASE_DIR, "12.mp3")

# Музыка
mixer.music.load(MUSIC_FILE)
mixer.music.play(-1)


# Класс Платнеты
class Planet:
    def __init__(self, screen, radius, orbit_radius, speed, image_path, angle=0):
        self.screen = screen
        self.radius = radius
        self.base_orbit = orbit_radius
        self.speed = speed
        self.angle = angle

        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (radius * 2, radius * 2))

        self.x = 0
        self.y = 0

    def update(self, dt, scale):
        global cx, cy
        self.angle += self.speed * dt
        orbit = self.base_orbit * scale
        self.x = cx + orbit * math.cos(self.angle)
        self.y = cy + orbit * math.sin(self.angle)

    def draw(self):
        self.screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))


# Планеты
speed_scale = 0.4

sun = Planet(screen, 70, 0, 0, SUN_IMAGE)

mercury = Planet(screen, 10, 100, 3.0 * speed_scale, MERCURY_IMAGE)
venus   = Planet(screen, 14, 130, 2.2 * speed_scale, VENUS_IMAGE)
earth   = Planet(screen, 16, 170, 0.9 * speed_scale, EARTH_IMAGE)
moon    = Planet(screen, 5, 35, 6.0 * speed_scale, MOON_IMAGE)
mars    = Planet(screen, 12, 220, 1.4 * speed_scale, MARS_IMAGE)
jupiter = Planet(screen, 30, 300, 1.0 * speed_scale, JUPITER_IMAGE)
saturn  = Planet(screen, 28, 350, 0.8 * speed_scale, SATURN_IMAGE)
uranus  = Planet(screen, 22, 380, 0.6 * speed_scale, URANUS_IMAGE)
neptune = Planet(screen, 22, 400, 0.5 * speed_scale, NEPTUNE_IMAGE)
pluto   = Planet(screen, 10, 420, 0.3 * speed_scale, PLUTO_IMAGE)

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto]


# Комета
class Comet:
    def __init__(self):
        self.active = False
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0

        self.image = pygame.image.load(COMET_IMAGE).convert()
        self.image = pygame.transform.scale(self.image, (60, 30))

    def start(self):
        self.active = True

        side = random.choice(["left", "right", "top", "bottom"])

        if side == "left":
            self.x = -200
            self.y = random.randint(0, HEIGHT)
        elif side == "right":
            self.x = WIDTH + 200
            self.y = random.randint(0, HEIGHT)
        elif side == "top":
            self.x = random.randint(0, WIDTH)
            self.y = -200
        elif side == "bottom":
            self.x = random.randint(0, WIDTH)
            self.y = HEIGHT + 200

        target_x = random.randint(-200, WIDTH + 200)
        target_y = random.randint(-200, HEIGHT + 200)

        speed = random.randint(300, 500)

        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.hypot(dx, dy)

        self.vx = dx / dist * speed
        self.vy = dy / dist * speed

    def update(self, dt):
        if self.active:
            self.x += self.vx * dt
            self.y += self.vy * dt
            if self.x < -300 or self.x > WIDTH + 300 or self.y < -300 or self.y > HEIGHT + 300:
                self.active = False

    def draw(self):
        if self.active:
            screen.blit(self.image, (int(self.x), int(self.y)))


comet = Comet()

# Основной цикл
running = True
while running:
    dt = clock.tick(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            cx = WIDTH // 2
            cy = HEIGHT // 2

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                comet.start()

    max_orbit = 450
    scale = min(WIDTH, HEIGHT) / (max_orbit * 2)

    sun.update(dt, 0)
    for p in planets:
        p.update(dt, scale)

    earth.update(dt, scale)
    moon.update(dt, scale * 0.3)

    moon.x = earth.x + (moon.base_orbit * scale * 0.6) * math.cos(moon.angle)
    moon.y = earth.y + (moon.base_orbit * scale * 0.6) * math.sin(moon.angle)
    moon.angle += moon.speed * dt

    comet.update(dt)

    screen.fill((0, 0, 20))

    sun.draw()

    for p in planets:
        p.draw()

    earth.draw()
    moon.draw()

    comet.draw()

    pygame.display.flip()

pygame.quit()

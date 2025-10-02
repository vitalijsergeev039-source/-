import pygame
pygame.init()
font = pygame.font.SysFont(None, 30)

screen = pygame.display.set_mode((477, 706))
pygame.display.set_caption("Еж в лесу")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((44,160,90))
    pygame.draw.polygon(screen, (108,93,83), [
        (0, 400), (477, 400), (477, 706), (0, 706), (0, 400)
         ])
    pygame.draw.polygon(screen, (212,170,0), [
        (0, 0), (36, 0), (36, 455), (0, 455), (0, 0)
         ])
    pygame.draw.polygon(screen, (212,170,0), [
        (62, 0), (176, 0), (176, 695), (62, 695), (62, 0)
         ])
    pygame.draw.polygon(screen, (212,170,0), [
        (338, 0), (384, 0), (384, 421), (338, 421), (338, 0)
         ])
    pygame.draw.polygon(screen, (212,170,0), [
        (440, 0), (472, 0), (472, 519), (440, 519), (440, 0)
         ])
    pygame.draw.ellipse(screen, (72,55,55), (259, 547, 160, 65))
    pygame.draw.ellipse(screen, (72,55,55), (382, 600, 20, 15))
    pygame.draw.ellipse(screen, (72,55,55), (271, 600, 20, 15))
    pygame.draw.ellipse(screen, (72,55,55), (250, 584, 20, 15))
    pygame.draw.ellipse(screen, (72,55,55), (405, 570, 40, 25))
    pygame.draw.circle(screen, (0, 0, 0), (445, 583), 2)
    pygame.draw.circle(screen, (0, 0, 0), (422, 584), 3)
    pygame.draw.circle(screen, (0, 0, 0), (427, 576), 3)
    pygame.draw.line(screen, (36,28,28), (240,547), (270,590), 3)
    pygame.draw.line(screen, (36,28,28), (245,547), (275,590), 3)
    pygame.draw.line(screen, (36,28,28), (250,547), (280,590), 3)
    pygame.draw.line(screen, (36,28,28), (255,547), (285,590), 3)
    pygame.draw.line(screen, (36,28,28), (260,547), (290,590), 3)
    pygame.draw.line(screen, (36,28,28), (265,547), (295,590), 3)
    pygame.draw.line(screen, (36,28,28), (270,547), (300,590), 3)
    pygame.draw.line(screen, (36,28,28), (275,547), (305,590), 3)
    pygame.draw.line(screen, (36,28,28), (280,547), (310,590), 3)
    pygame.draw.line(screen, (36,28,28), (285,547), (315,590), 3)
    pygame.draw.line(screen, (36,28,28), (290,547), (320,590), 3)
    pygame.draw.line(screen, (36,28,28), (295,547), (325,590), 3)
    pygame.draw.line(screen, (36,28,28), (300,547), (330,590), 3)
    pygame.draw.line(screen, (36,28,28), (305,547), (335,590), 3)
    pygame.draw.line(screen, (36,28,28), (310,547), (340,590), 3)
    pygame.draw.line(screen, (36,28,28), (315,547), (345,590), 3)
    pygame.draw.line(screen, (36,28,28), (320,547), (350,590), 3)
    pygame.draw.line(screen, (36,28,28), (325,547), (355,590), 3)
    pygame.draw.line(screen, (36,28,28), (330,547), (360,590), 3)
    pygame.draw.line(screen, (36,28,28), (335,547), (365,590), 3)
    pygame.draw.line(screen, (36,28,28), (340,547), (370,590), 3)
    pygame.draw.line(screen, (36,28,28), (345,547), (375,590), 3)
    pygame.draw.line(screen, (36,28,28), (350,547), (380,590), 3)
    pygame.draw.line(screen, (36,28,28), (355,547), (385,590), 3)
    pygame.draw.line(screen, (36,28,28), (360,547), (390,590), 3)
    pygame.draw.line(screen, (36,28,28), (365,547), (395,590), 3)
    pygame.draw.line(screen, (36,28,28), (370,547), (400,590), 3)
    pygame.draw.line(screen, (36,28,28), (375,547), (405,590), 3)
    pygame.draw.line(screen, (36,28,28), (380,547), (410,590), 3)
    pygame.draw.line(screen, (36,28,28), (385,547), (415,590), 3)
    pygame.draw.line(screen, (36,28,28), (265,570), (295,525), 3)
    pygame.draw.line(screen, (36,28,28), (270,570), (300,525), 3)
    pygame.draw.line(screen, (36,28,28), (275,570), (305,525), 3)
    pygame.draw.line(screen, (36,28,28), (280,570), (310,525), 3)
    pygame.draw.line(screen, (36,28,28), (285,570), (315,525), 3)
    pygame.draw.line(screen, (36,28,28), (290,570), (320,525), 3)
    pygame.draw.line(screen, (36,28,28), (295,570), (325,525), 3)
    pygame.draw.line(screen, (36,28,28), (300,570), (330,525), 3)
    pygame.draw.line(screen, (36,28,28), (305,570), (335,525), 3)
    pygame.draw.line(screen, (36,28,28), (310,570), (340,525), 3)
    pygame.draw.line(screen, (36,28,28), (315,570), (345,525), 3)
    pygame.draw.line(screen, (36,28,28), (320,570), (350,525), 3)
    pygame.draw.line(screen, (36,28,28), (325,570), (355,525), 3)
    pygame.draw.line(screen, (36,28,28), (330,570), (360,525), 3)
    pygame.draw.line(screen, (36,28,28), (335,570), (365,525), 3)
    pygame.draw.line(screen, (36,28,28), (340,570), (370,525), 3)
    pygame.draw.line(screen, (36,28,28), (345,570), (375,525), 3)
    pygame.draw.line(screen, (36,28,28), (350,570), (380,525), 3)
    pygame.draw.line(screen, (36,28,28), (355,570), (385,525), 3)
    pygame.draw.line(screen, (36,28,28), (360,570), (390,525), 3)
    pygame.draw.line(screen, (36,28,28), (365,570), (395,525), 3)
    pygame.draw.line(screen, (36,28,28), (370,570), (400,525), 3)
    pygame.draw.line(screen, (36,28,28), (375,570), (405,525), 3)
    pygame.draw.line(screen, (36,28,28), (380,570), (410,525), 3)
    pygame.draw.line(screen, (36,28,28), (385,570), (415,525), 3)
    pygame.draw.line(screen, (36,28,28), (390,570), (420,525), 3)
    pygame.draw.line(screen, (36,28,28), (395,570), (425,525), 3)
    pygame.draw.line(screen, (36,28,28), (400,570), (430,525), 3)
    pygame.draw.line(screen, (36,28,28), (405,570), (435,525), 3)
    pygame.draw.circle(screen, (200,113,55), (283, 563), 16)
    pygame.draw.circle(screen, (200,113,55), (300, 550), 16)
    pygame.draw.circle(screen, (255,0,0), (380, 560), 25)
    pygame.draw.ellipse(screen, (255,255,255), (333, 533, 15, 45))
    pygame.draw.ellipse(screen, (255,0,0), (319, 520, 45, 15))
    mx, my = pygame.mouse.get_pos()
    text = font.render(f"x: {mx}, y: {my}", True, (0, 0, 0))
    screen.blit(text, (10, 10))


    pygame.display.flip()
    

pygame.quit()
    
    
    
    
    






    

    
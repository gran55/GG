import pygame

W = 1080
H = 672
BLUE = (0, 0, 0)
move = 1
block = 0
start = 1

pygame.init()
pygame.display.set_caption("текст")
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 28, True, False)
font_box = pygame.Surface((W - font.get_height(), font.get_height()))
font_rect = font_box.get_rect(center=(W // 2, H - font.get_height()))
font2 = pygame.font.SysFont('Arial', 14, False, True,) 


FOM = pygame.image.load('FOM.png')
FOM_rect = FOM.get_rect(topleft=(0, 0))

FON = pygame.image.load('FON.png')
FON_rect = FON.get_rect(topleft=(0, 0))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
            elif e.key == pygame.K_3:



        screen.blit(FOM, FOM_rect)
        screen.blit(FON, FON_rect)
        pygame.display.update()


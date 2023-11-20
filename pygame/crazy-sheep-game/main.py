import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Crazy Sheep')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('Ground.png').convert()
text_surface = test_font.render('Crazy Sheep Game', False, 'Black')

dirt_surface = pygame.image.load('grass.png').convert()
dirt_rect = dirt_surface.get_rect(midbottom = (0, 0))

player_surf = pygame.image.load('sheep.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

class Dirt:
    def __init__(self,xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.dirtimage = pygame.image.load('grass.png').convert()
        self.dirtrect = self.dirtimage.get_rect()
    def getSurf(self):
        return self.dirtimage
    def changeXY(self,xpos,ypos):
        self.x = xpos
        self.y = ypos

dirts = []
multiplier = 0
for i in range(4):
    dirts.append(Dirt(300 + (96 * multiplier), 0))
    multiplier += 1

dirt_y_pos = 5
speed = 4
move_down = True
bottom = 400 - 96
pause = False
index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            index += 1
            dirt_y_pos = 0
            if index >= len(dirts):
                index = 0

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(player_surf, player_rect)
    screen.blit(text_surface, (300, 50))

    for dirt in dirts:
        screen.blit(dirt.getSurf(), (dirt.x, dirt.y))

    if move_down:
        dirt_y_pos += speed
    else:
        dirt_y_pos -= speed

    if dirt_y_pos <= 0:
        move_down = True
    elif dirt_y_pos >= bottom:
        move_down = False

    dirts[index].changeXY(dirts[index].x, dirt_y_pos)
    screen.blit(dirts[index].getSurf(), (dirts[index].x, dirts[index].y))

    pygame.display.update()
    clock.tick(60)

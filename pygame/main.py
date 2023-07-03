import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner Tutorial')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Pixeltype.ttf', 50)

sky_surface = pygame.image.load('Sky.png').convert()
ground_surface = pygame.image.load('Ground.png').convert()
text_surface = test_font.render('MY GAME', False, 'Black')

jaguar_surface = pygame.image.load('jaguar.png').convert_alpha()
jaguar_rect = jaguar_surface.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('sloth1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0, 300))
    screen.blit(text_surface,(300, 50))
    
    jaguar_rect.x -= 4
    if jaguar_rect.right <= 0: 
        jaguar_rect.left = 800
    screen.blit(jaguar_surface, jaguar_rect)
    player_rect.left += 1
    screen.blit(player_surf,player_rect)

    if player_rect.colliderect(jaguar_rect):
        print('collision')

    # draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(60)
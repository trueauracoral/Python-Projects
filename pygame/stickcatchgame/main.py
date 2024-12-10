import pygame
import random
from sys import exit

# Initialize pygame
pygame.init()

# Logical screen dimensions
LOGICAL_WIDTH = 113
LOGICAL_HEIGHT = 80
SCALE_FACTOR = 4  # Scale by 4 times

# Create the window with the scaled size
WINDOW_WIDTH = LOGICAL_WIDTH * SCALE_FACTOR
WINDOW_HEIGHT = LOGICAL_HEIGHT * SCALE_FACTOR
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Stick Catch Game')
clock = pygame.time.Clock()

roundringimage = pygame.image.load('roundring.png').convert()
test_font = pygame.font.Font('3-by-5-pixel-font.ttf', 8)

logical_surface = pygame.Surface((LOGICAL_WIDTH, LOGICAL_HEIGHT))
FINISHED = False

# Stick class
class Stick:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
        self.velocity_y = 0  # Vertical velocity
        self.gravity = 0.01
        self.stickimage = pygame.image.load('stick.png').convert_alpha()
        self.stickrect = self.stickimage.get_rect()
        self.stickrect.topleft = (self.x, self.y)

    def get_surf(self):
        return self.stickimage

    def change_xy(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

    def update(self):
        self.velocity_y += self.gravity
        self.y += self.velocity_y
        self.stickrect.topleft = (self.x, self.y)

# Create sticks
sticks = []
stickHeight = 8
heightList = [0, 1, 2, 2, 3]
heightList = heightList + heightList[::-1]
for num, i in enumerate(range(10)):
    sticks.append(Stick(18 + (8 * i), stickHeight + heightList[num]))  # Adjusted for logical scale

# Game variables
dirt_y_pos = 5
speed = 1  # Adjust for logical scale
move_down = True
bottom = LOGICAL_HEIGHT - 24  # Adjust for logical scale
pause = False
index = random.randint(0, 9)
timer_active = False
timer_start = 0
timer_duration = 2000
counter = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if sticks[index].stickrect.collidepoint((event.pos[0]/SCALE_FACTOR, event.pos[1]/SCALE_FACTOR)):
                print("AAAA")
                counter+=1

    # Fill the logical surface
    logical_surface.fill((0, 0, 0))  # Black background
    logical_surface.blit(roundringimage, (LOGICAL_WIDTH/2-roundringimage.get_width()/2, 3))

    text_surface = test_font.render(str(counter).zfill(2), False, (245, 27, 27))
    logical_surface.blit(text_surface, (53, 44))

    # Draw sticks
    for dirt in sticks:
        logical_surface.blit(dirt.get_surf(), (dirt.x, dirt.y))

    # Move the stick
    if not FINISHED:
        if sticks[index].y >= LOGICAL_HEIGHT:
            sticks.pop(index)
            timer_active = True
            timer_start = pygame.time.get_ticks()
            if len(sticks) > 0:
                index = random.randint(0, len(sticks) - 1)
            else:
                FINISHED = True

        if timer_active:
            elapsed_time = pygame.time.get_ticks() - timer_start
            if elapsed_time >= timer_duration:
                timer_active = False

        if not timer_active and not FINISHED:
            sticks[index].update()
            logical_surface.blit(sticks[index].get_surf(), (sticks[index].x, sticks[index].y))

    # Scale and blit the logical surface onto the screen
    scaled_surface = pygame.transform.scale(logical_surface, (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(scaled_surface, (0, 0))

    # Update the display
    pygame.display.update()
    clock.tick(60)

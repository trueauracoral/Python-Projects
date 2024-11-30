import pygame
pygame.init()

screen = pygame.display.set_mode((450, 600))

timer_font = pygame.font.Font("04B_19__.ttf", 38)
timer_sec = 0
timer_min = 0
timer_text = timer_font.render("00:00", True, (255, 255, 255))

# USEREVENTS are just integers
# you can only have like 31 of them or something arbitrarily low
timer = pygame.USEREVENT + 1
pygame.time.set_timer(timer, 50)    # sets timer with USEREVENT and delay in milliseconds

running = True
texter = "Click at 10:00"
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (mouse_x < 175 + 110) and (mouse_x > 175) and (mouse_y > 160) and (mouse_y < 160+100):
                print("HELLO")
                pygame.time.set_timer(timer, 0)
                if (timer_min == 10) and (timer_sec == 1):
                    texter = "HOORAY"

            if event.button == 1:
                print("Left click at:", mouse_x, mouse_y)
        if event.type == timer:
            if timer_sec < 60:
                timer_text = timer_font.render("%02d:%02d" % (timer_min, timer_sec), True, (212, 55, 55))
                timer_sec += 1
            else:
                timer_min += 1
                timer_sec = 0

    screen.blit(timer_text, (175, 20))

    startX = 140

    pygame.draw.rect(screen, (181, 119, 33), (startX, 125, 160, 20))
    pygame.draw.rect(screen, (240, 162, 55), (startX, 145, 160, 140))
    pygame.draw.circle(screen, (153, 37, 37), (startX+80,140+70),50)
    pygame.draw.circle(screen, (212, 55, 55), (startX+80,140+80),50)

    print(timer_min)
    print(timer_sec)
    instructionsText = timer_font.render(texter, True, (255, 255, 255))
    screen.blit(instructionsText, (40, 375))

    pygame.display.update()

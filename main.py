import pygame

# pygame setup
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen_colour = "white"
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
CLOCK = pygame.time.Clock()
running = True
FPS = 60

# running
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # defines the key pressed each frame
    keys = pygame.key.get_pressed()
    
    if (keys[pygame.K_SPACE]):
        pass



    # flip() the display to put the work on screen
    pygame.display.flip()

    # limits FPS to 60
    CLOCK.tick(FPS)

pygame.quit()
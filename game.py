import pygame, random

#Initialize
pygame.init()

#Set Display
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ghost Catcher")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update display and tick clock
    pygame.display.update
    clock.tick(FPS)


#End game
pygame.quit()
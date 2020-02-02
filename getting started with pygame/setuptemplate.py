"""
SKELETON FOR NEW PYGAME
"""
import pygame
import random

#presets for window
windowWidth = 360
windowHeight = 480
FPS = 30

CYAN = (0,255,255)

"""
MAKES WINDOW
"""
#starts pygame, but does not open window
pygame.init()
#starts the sound program
pygame.mixer.init()

#this code however is for displaying
screen = pygame.display.set_mode((windowWidth, windowHeight))
#this puts the title on the window
pygame.display.set_caption("THE GAME!")
#makes shure FSP is set, will use later
clock = pygame.time.Clock()


"""
GAME LOOP
"""
running = True
# just so we can eazy end the game
while running:
    #makes shure the loop runs the same on all PCs
    clock.tick(FPS)
    """
    PROCESS EVENTS:
    here is where you put key pressing
    """
    #the for loop gets the events that have happend since last time
    #usefull for key pressing, so a keypress will not get ignored if pressed other place in game loop
    for event in pygame.event.get():
        #checks for closing window with x in corner
        if event.type == pygame.QUIT:
            running = False
    """
    UPDATE:
    here is where you put what needs to be calculated
    """
    """
    RENDER:
    here you put what needs to go on screen
    """
    #put the colour you want in the () of fill
    # the fill takes RGB
    # (255,255,255) = White, and (0,0,0) = Black
    #screen.fill((0,255,255)) could be used but we can define them in presets
    # for later use
    screen.fill(CYAN)
    #to do less prosessing for the screen, we use display.flip to display after we are done
    #with everything we want to show
    #always do this last
    pygame.display.flip()
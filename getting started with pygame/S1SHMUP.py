"""
SKELETON FOR NEW PYGAME
"""
import pygame
import random
import os

#presets for window
#some presets are 360x480 (small) 800x600 (medium)
windowWidth = 480
windowHeight = 600
FPS = 30

#some usefull colors
CYAN = (0,255,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

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
CREATING SPRITE
"""
#pygame already has a sprite library so we will get from there
class Player(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = windowWidth/2
        self.rect.bottom = windowHeight -10
        self.speedx = 0

    def update(self):
        #you always whant the speed to be 0 unless something else happens
        self.speedx = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -15
        if keystate[pygame.K_RIGHT]:
            self.speedx = 15

        self.rect.x += self.speedx

        if self.rect.right > windowWidth:
            self.rect.right = windowWidth
        if self.rect.left < 0:
            self.rect.left = 0


"""
Sprite group:
usefull for minimizing code and pygame can rund multiple sprites faster this way
all we have to put in UPDATE is now all_sprites.update()
all we put in RENDER is all_sprites.draw()
"""
all_sprites = pygame.sprite.Group()
#makes an instance of the Player class to add a sprite
player = Player()
#adds it to the group
all_sprites.add(player)




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
    here is where you put what needs to be calculated, what the sprite should do
    """
    #updates the rules for all sprites
    all_sprites.update()
    """
    RENDER:
    here you put what needs to go on screen
    """
    #put the colour you want in the () of fill
    # the fill takes RGB
    # (255,255,255) = White, and (0,0,0) = Black
    #screen.fill((0,255,255)) could be used but we can define them in presets
    # for later use
    screen.fill(BLACK)

    #updates all the sprites from the sprite group
    #needs to put where (screen)
    all_sprites.draw(screen)


    #to do less prosessing for the screen, we use display.flip to display after we are done
    #with everything we want to show
    #always do this last
    pygame.display.flip()
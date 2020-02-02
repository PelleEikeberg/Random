"""
SHMUP GAME
"""
import pygame
import random
import os

#presets for window
#some presets are 360x480 (small) 800x600 (medium)
windowWidth = 480  
windowHeight = 600
FPS = 60

CYAN = (0,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

"""
SET UP ASSETS: game sound and images
"""
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "IMG")



"""
MAKES WINDOW
"""
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("SHMUP!")
clock = pygame.time.Clock()

"""
CREATING SPRITE
"""
class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.y_speed = 5


        self.rect.center = (windowWidth/2, windowHeight/2)

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        #this is what makes the sprite update back to the other side.
        if self.rect.left > windowWidth:
            self.rect.right = 0
        if self.rect.bottom > windowHeight-200:
            self.y_speed = -5
        if self.rect.bottom < 200:
            self.y_speed = 5



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
    screen.fill(BLUE)

    #updates all the sprites from the sprite group
    #needs to put where (screen)
    all_sprites.draw(screen)


    #to do less prosessing for the screen, we use display.flip to display after we are done
    #with everything we want to show
    #always do this last
    pygame.display.flip()
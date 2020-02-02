"""
SKELETON FOR NEW PYGAME
"""
import pygame
import random
from os import path

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
YELLOW = (255,255,0)


#usefull folders
img_dir = path.join(path.dirname(__file__), "IMG")

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
        #this loads the image we want, the size can be toggled
        #but it is usefull to check the parameters is not stretched
        self.image = pygame.transform.scale(player_img, (50,38))

        self.image.set_colorkey(BLACK)

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

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)

        all_sprites.add(bullet)
        bullets.add(bullet)


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()

        #picking random x coors to be somewhere in the window x range.
        self.rect.x = random.randrange(0, windowWidth - self.rect.width)

        #we want it to spawn of the screen so we choose some where -y (-40) caouse of self.image size
        self.rect.y = random.randrange(-100, -40)

        self.speedy = random.randrange(5, 15)
        self.speedx = random.randrange(-5,5)

    
    def update(self):

        self.rect.y += self.speedy
        self.rect.x += self.speedx

        #what to do if it hits the ground?
        #spawns again
        if self.rect.top > windowHeight + 10 or self.rect.left < -25 or self.rect.right > windowWidth +25:
            self.rect.x = random.randrange(0, windowWidth - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 15)





class Bullet(pygame.sprite.Sprite):
    #for once the init is not blank! the x,y is determended by the player later
    #the bullet we want is comming out of the player.
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.rect.bottom = y
        self.rect.centerx = x
        #we want faster speed that mobs or player (can tweak later)
        self.speedy = -20


    def update(self):
        self.rect.y += self.speedy

        #kill if off the screen
        if self.rect.bottom < 0:
            #removes it from any group aswell
            self.kill()




"""
load game grafixs
"""
background = pygame.image.load(path.join(img_dir, "starry.png")).convert()
background_rect = background.get_rect()

player_img = pygame.image.load(path.join(img_dir, "playerShip1_blue.png")).convert()

meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown_med1.png")).convert()
laser_img = pygame.image.load(path.join(img_dir, "laserGreen12.png")).convert()


"""
Sprite group:
usefull for minimizing code and pygame can rund multiple sprites faster this way
all we have to put in UPDATE is now all_sprites.update()
all we put in RENDER is all_sprites.draw()
"""
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
#makes an instance of the Player class to add a sprite
player = Player()
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
        

    """
    UPDATE:
    here is where you put what needs to be calculated, what the sprite should do
    """
    #updates the rules for all sprites
    all_sprites.update()


    #unlike the spritecollide, this checks for any from one group hits any from other group
    #does the mob get deleted? True, does the bullet get deleted? True
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    #but now we run out of mobs. to spawn more we do the following
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)


    #check if a mob hits a player
    #spritecollide(what collides, what group)
    #chould the collide be deleted = False
    hits = pygame.sprite.spritecollide(player, mobs, False)
    #if hits =[] is the same as false
    if hits:
        running = False
    """
    RENDER:
    here you put what needs to go on screen
    """
    #put the colour you want in the () of fill
    # the fill takes RGB
    # (255,255,255) = White, and (0,0,0) = Black
    #screen.fill((0,255,255)) could be used but we can define them in presets
    # for later use
    #screen.fill is always usefull if we fail in loading image.
    screen.fill(BLACK)
    #this loads the background image
    screen.blit(background, background_rect)


    #updates all the sprites from the sprite group
    #needs to put where (screen)
    all_sprites.draw(screen)


    #to do less prosessing for the screen, we use display.flip to display after we are done
    #with everything we want to show
    #always do this last
    pygame.display.flip()
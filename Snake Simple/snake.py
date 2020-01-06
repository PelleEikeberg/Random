from pygame.locals import *
import pygame
from time import sleep

class Player():
    def __init__(self, x=10, y=10, speed=10, direction=0):
        self.x = x; self.y = y; self.speed = speed; self.direction = direction
    

    def update(self):
        if self.direction == 0:
            self.x = self.x + self.speed
        if self.direction == 1:
            self.x = self.x - self.speed
        if self.direction == 2:
            self.y = self.y - self.speed
        if self.direction == 3:
            self.y = self.y + self.speed



    def moveRight(self):
        self.direction = 0
    
    def moveLeft(self):
        self.direction = 1
    
    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3



class App():

    windowWidth = 800  
    windowHeight = 600
    player = 0 

    def __init__(self):
        self._running = True # used to deremed to run the window or not
        self._display_surf = None
        self._image_surf = None
        self.player = Player() # Player is the class with movements
    
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        #whatever that will be the title of the window.
        pygame.display.set_caption('Pygame Snake')
        self._running = True
        # the image.load("string") will try to load from same folder as program, so have the file ready
        # in this case the image will be one ´block´ of the snake.
        self._image_surf = pygame.image.load("hei.png").convert()
    
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    
    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        pygame.display.flip()
    
    def on_cleanup(self):
        pygame.quit()
    
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            if (keys[K_RIGHT]):
                self.player.moveRight()
            if (keys[K_LEFT]):
                self.player.moveLeft()
            if (keys[K_UP]):
                self.player.moveUp()
            if (keys[K_DOWN]):
                self.player.moveDown()
            
            self.player.update()
            """
            if the player() does not have update() and just have the movement
            code in the move...() instead it will move the same, but with update
            the block will move the giver direction without stopping.
            """
            self.on_loop()
            self.on_render()
            sleep(100/1000)
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
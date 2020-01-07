from pygame.locals import *
import pygame
from time import sleep
from random import randint

class Player():
    def __init__(self, x=[0], y=[0], speed=44, direction=0, length=3):
        self.x = x; self.y = y; self.speed = speed; self.direction = direction
        self.length = length

        self.updatecountMAx = 2
        self.updatecount = 0

        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)
        self.x[1] = 1*44
        self.x[2] = 2*44

    def border(self):
        if self.x >= 800:
            self.x = 800
        


    def update(self):

        self.updatecount += 1
        if self.updatecount < self.updatecountMAx:

            #moves previous block to head possision
            for i in range(self.length-1, 0, -1):
                #print("self.x[", str(i), "] = self.x[", str(i-1), "]")
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            #updates the ´head´
            if self.direction == 0:
                self.x[0] = self.x[0] + self.speed
            if self.direction == 1:
                self.x[0] = self.x[0] - self.speed
            if self.direction == 2:
                self.y[0] = self.y[0] - self.speed
            if self.direction == 3:
                self.y[0] = self.y[0] + self.speed

            self.updatecount = 0

    def moveRight(self):
        self.direction = 0
    
    def moveLeft(self):
        self.direction = 1
    
    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3


    def draw(self, surface, image):
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))


class Apple():
    def __init__(self, x=0, y=0, speed=44):
        self.x = x*speed
        self.y = y*speed
    
    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))




class Rules():
    def isCollision(self, x1, y1, x2, y2, bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False



class App():
    def __init__(self):
        self._running = True # used to deremed to run the window or not
        self._display_surf = None
        self._image_surf = None
        self.player = Player(length=10) # Player is the class with movements
    
        self.windowWidth = 800  
        self.windowHeight = 600

        self.apple = Apple(x=5, y=5)

        self.rules = Rules()


    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        #whatever that will be the title of the window.
        pygame.display.set_caption('Pygame Snake')
        self._running = True
        # the image.load("string") will try to load from same folder as program, so have the file ready
        # in this case the image will be one ´block´ of the snake.
        self._image_surf = pygame.image.load("hei.png").convert()

        self._apple_surf = pygame.image.load("hei2.png").convert()
    
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
    
    def on_loop(self):
        self.player.update()


        #does the head bite the apple?
        for i in range(0, self.player.length):
            if self.rules.isCollision(self.apple.x, self.apple.y, self.player.x[i], self.player.y[i], 44):
                self.apple.x = randint(2,9)*44
                self.apple.y = randint(2,9)*44
                self.player.length += 1
        
        #does the snake bite itself?
        for i in range(2, self.player.length):
            if self.rules.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 40):
                print("you failed")
                exit()
    
        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        #self._display_surf.blit(self._image_surf, (self.player.x, self.player.y))
        #pygame.display.flip()
        self.apple.draw(self._display_surf, self._apple_surf)
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
            
            if (keys[K_ESCAPE]):
                self._running = False
            #self.player.update()
            """
            if the player() does not have update() and just have the movement
            code in the move...() instead it will move the same, but with update
            the block will move the giver direction without stopping.
            """
            self.on_loop()
            self.on_render()
            sleep(50/1000)
        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
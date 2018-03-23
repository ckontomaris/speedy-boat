'''
Created on Feb 17, 2018

@author: ckont
'''
import pygame
import time

# last tutorial: https://www.youtube.com/watch?v=dX57H9qecCU

pygame.init()

# resolution of game, tuple of width x height
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

black = (0, 0, 0)
# 256 options, including 0
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
light_blue = (56, 255, 200)

boatImg = pygame.image.load('transBoat.png')


# put boat in background display
# x,y must be in tuple
def boat(x, y):
    gameDisplay.blit(boatImg, (x, y))


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 70)
    # place text with rectange
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    # restart everything
    game_loop()

    
def text_objects(text, Font):
    textSurface = Font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash():
    message_display("You sunk!")
    

def game_loop():

    # starting point
    x = (display_width * 0.4)
    y = (display_height * 0.8)
    boat(x, y)
    x_change = 0
    car_width = 73
    # coordinate system review
    # 0,0 is top left
    # as you add to x, you move right
    # as you add to y, you move down
    
    # title of window
    pygame.display.set_caption("speedster af")
    
    # clock times things (fps)
    clock = pygame.time.Clock()
    
    # game loop is logic for the game, needs a way to stop (crashing)
    gameExit = False
    
    while not gameExit:
        # gets any event (click, keyboard, etc), per frame
        # quit is when you click the X
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0 
            #print(event)
        # we have to paint white FIRST
        gameDisplay.fill(light_blue)
        boat(x, y)
        x += x_change
        # after the car is drawn, now we crash
        
        # x is the top left of the image, so we need to account for that
        if x > display_width - car_width or x < 0:
            crash()
        # updates the thing in parameter
        pygame.display.update()
        # how fast is this updating? (put FPS at a parameter)
        clock.tick(60)

    
# quitting pygame and python
game_loop()
pygame.quit()
quit()

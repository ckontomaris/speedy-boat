'''
Created on Feb 17, 2018

@author: ckont
'''
import pygame
import time
import random

# last tutorial: https://www.youtube.com/watch?v=dX57H9qecCU

pygame.init()

# resolution of game, tuple of width x height
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

black = (0, 0, 0)
# 256 color options, including 0
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
light_blue = (56, 255, 200)

boatImg = pygame.image.load('transBoat.png')


# put boat in background display
# x,y must be in tuple
# blit is the command?
def boat(x, y):
    gameDisplay.blit(boatImg, (x, y))

#function that displays a message in the center
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

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+ str(count), True, black)
    gameDisplay.blit(text, (0,0))

#where the blocks get made
def things(x, y, width, height, color):
    #specify shape, location, color

    #i made the blocks way bigger, not in video
    pygame.draw.rect(gameDisplay, red, [x,y, width,height])

#says you sunk and restarts the game
def crash():
    message_display("You sunk!")

# how the game actually runs
def game_loop():

    # starting point
    x = (display_width * 0.4)
    y = (display_height * 0.8)
    boat(x, y)
    x_change = 0

    #the first obsticale
    thing_startx = random.randrange(0 , display_width)
    #we want it to start above the screen
    thing_starty = -600
    thing_speed = 7
    #its a 100 by 100 square
    thing_width = 100
    thing_height = 100
    dodged = 0;

    car_width = 70
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

        #draw the boxes
        things(thing_startx, thing_starty,thing_width,thing_height, black)
        #move the boxes up and down
        #the speed is the amount that we want to move the box up by
        thing_starty += thing_speed


        boat(x, y)
        x += x_change

        things_dodged(dodged)

        # x is the top left of the image, so we need to account for that
        if x > display_width - car_width or x < 0:
            crash()


        #as soon as the block gets off the screen,
        #make another one show up immedietly
        if thing_starty> display_height:
            thing_starty= 0 -thing_height
            #we need to randomize where the next one comes in
            thing_startx=random.randrange(0,display_width)
            dodged+=1
            thing_speed += 1
            thing_width += dodged*1.2



        #we need to make sure there is actual intersect
        #the x AND Y need to intersect
        #thing start y is the top, we need to add the height of the box
        #made in video 7
        if y<thing_starty+thing_height:

            if x>thing_startx and x<thing_startx + thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                print("x crossover")
                crash()



        # updates the thing in parameter
        pygame.display.update()
        # how fast is this updating? (put FPS at a parameter)
        clock.tick(60)


# quitting pygame and python
game_loop()
pygame.quit()
quit()

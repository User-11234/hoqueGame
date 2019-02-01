"""
This is the snake game. Learnt from newboston python tutorial.
You need pygame on your computer.
Search "pygame" on https://www.google.com
"""

#mod3: new snake color
#mod4: new ackground color
#mod5: new apple color

import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
purple = (213,106,216)
red = (250,0,0)
green = (0, 150, 0)
blue = (0, 0, 200)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SnakeyBoi')

img = pygame.image.load('snakehead2.png')

clock = pygame.time.Clock()

block_size = 20
FPS = 15

direction = "right"

smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",40)
largefont = pygame.font.SysFont("comicsansms",80)

def game_intro():

    gameExit = False

    intro = True

    count = 0

    titleColor = white

    while intro:
        gameDisplay.fill(black)
        message_to_screen("Time to become a SnakeyBoi",
                          titleColor,
                          -20,
                          "medium")
        message_to_screen("Eat food to become longer!",
                          blue,
                          100)
        message_to_screen("Press enter to start",
                          red,
                          50)
        #Modified2: Made title screen blink.
        speed = 100
        count += 1


        if count > speed:
            count = 0

        if count == speed/2:
            titleColor = purple
        if count == speed:
            titleColor = white
            
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    intro = False

        pygame.display.update()

    gameLoop()
            
                
def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
        
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, black, [XnY[0],XnY[1],block_size,block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():

    global direction

    gameExit = False

    gameOver = False
    
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game over" ,
                              white,
                              y_displace= -50,
                              size = "large")
            message_to_screen("Press C to play again or Q to quit.",
                              purple,
                              y_displace = 20,
                              size = "small")
            #Modified1: I added a score for the snake game.
            message_to_screen("Score:" + str(len(snakeList)),
                              white,
                              y_displace = 100,
                              size = "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()


            
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x <0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
                    
        lead_x += lead_x_change
        lead_y += lead_y_change
        
        gameDisplay.fill(purple)

        AppleThickness = 30
        pygame.draw.rect(gameDisplay, white, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

            

        snake(block_size, snakeList)

        pygame.display.update()

##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
##                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
##                snakeLength += 1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:            
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
                snakeLength += 1                

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()

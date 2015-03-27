import pygame                    #imports for modules used in the programm
import time
import random
pygame.init()                    #starting pygame the module (ready to do stuff)

white = (255,255,255)            #colours that are later used in the game 
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width = 800              #windows sizes
display_height  = 600

gameDisplay = pygame.display.set_mode((display_width,display_height)) ##surface object
pygame.display.set_caption('Slither')                  #game name





clock = pygame.time.Clock()                          #setting the FPS from pygame module

block_size = 10                                  # how big the snake is (its a square so width and height are both 10)
FPS = 15                                            #framerate of the game


font = pygame.font.SysFont(None, 25)                   #setting font for text used in the game

def snake(block_size, snakelist):                     #defines the snake function that draws it and uses the list and draws a 10x10 green square (snake head)
     for XnY in snakelist:
         pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])

def message_to_screen(msg, color):                     #defines the message function that displays stuff to the user
    screen_text = font.render(msg, True, color)         
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])


def gameLoop():                                       #starts the game loop where the main functions are called and where most of the cool shit happens
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    
    
    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0           #random apple spawn locations
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
    
    while not gameExit:

        while gameOver == True:                                                          #gameover functionality loop which interrupts with a message if the player hits a side 
            gameDisplay.fill(white)
            message_to_screen("Game over , press C to play again or Q to quit", red)      #uses the predifined message_to_screen function to talk to the player and gives him the choice to restart or quit
            pygame.display.update()


            for event in pygame.event.get():                                            #event handling loop for quit functionality e.g q quits , c restarts
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()                                 #restarts game if player chooses quit

        
        
        for event in pygame.event.get():                                    #MAIN EVENT HANDLING LOOP IMPORTANT UP DOWN LEFT RIGHT TO MOVE THE SNAKE
            
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0




        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:                                   #border of screen collision detection
            gameOver = True
        


        
           
        lead_x += lead_x_change                                                         ##snake movement
        lead_y += lead_y_change



        
        gameDisplay.fill(white)                                                              #filling the screen white for the game
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])           #drawing the apple red from random predefined coordinates rounded to the nearest 10

                                                                                         #lists for the snake getting longer when he eats the apple (not fully implemented yet                                                                 
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)


        if len(snakeList) > snakeLength:
            else snakeList [0]
            
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:

                
                gameOver = True
        

        
        snake(block_size, snakeList)


    

        
        pygame.display.update()

        


        if lead_x == randAppleX and lead_y == randAppleY:                                                  ##loop for collsion detection with the apple if the player meets the apple it will respawn 
            
            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
            snakeLength += 1
        clock.tick(FPS)
         
                
                

            #print(event)


    pygame.quit()                                                                                             
    quit()


gameLoop()                                                                                          #calling the main game loop function











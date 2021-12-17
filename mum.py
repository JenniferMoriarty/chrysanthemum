#Chrysanthemum code
#by Dr. J. Moriarty, 10/9/20
#feel free to use for educational purposes
#dynamicsofanasteroid.com
import pygame
import math
pygame.init()  
pygame.display.set_caption("Chrysanthemum")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
clock = pygame.time.Clock() #sets up a game clock to regulate game speed

#these are timers for the game loops below
k=0
i=5;
doExit = False

#also tickers, but to handle oscillating color values
ticker = 0
color1 = 0
color2=255
adder = .5


while not doExit:#game loop
    #screen.fill((0, 0, 0)) #clear screen between loops
    clock.tick(60) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program
         
    k=0
    i+=math.pi/12
    while k < math.pi*2:
        pygame.draw.ellipse(screen, (color2/2,0,color1), (i*math.sin(k+i)+250, i*math.cos(k+i)+250, 300,300),5)
        k+=(math.pi/3)
        #lines 34-39 just handle color rotations
        ticker+=1
        if ticker >255:
            adder*=-1
            ticker = 1
        color1+=adder
        color2-=adder
        
        pygame.display.flip() 


#####################################end game loop   
pygame.quit()





import pygame
import time
from math import sin, cos, pi
pygame.init()

display_width =1024
display_height = 600

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Fourier')

black = (0,0,0)
white = (255,255,255)
red= (255,0,0)
green= (0,255,0)
blue= (0,0,255)
grey=(128,128,128)
linepoints = [] 


clock = pygame.time.Clock()

def circle(centre, radius, colour):
    pygame.draw.circle(screen, colour, centre, radius, 1)
def line(points, colour):
    pygame.draw.lines(screen, colour, False, points, 2)

def coeffs(n):
    if n == 0:
        return 0
    else:
        return 8/((pi*n)**3) * ((pi*n)**2+2*cos(n*pi)-2)

def game_loop():
    removing =False
    drawn = False
    gameExit=False
    i=0
    accuracy = 3
    scale=50
    period = 2
    locii=[]
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                #Allows the accuracy to be increased while running
                if event.key == pygame.K_LEFT:
                    if accuracy>2:
                        accuracy -=1
                        locii=[]
                        i=0
                elif event.key == pygame.K_RIGHT:
                    accuracy +=1
                    locii=[]
                    i=0
        
        
        #Creates a base circle with a fixed cenrte
        circles=[[[5*display_width//16,display_height//2],0]]
        
        #Finds the centres and radii of the circles 
        for j in range(1,accuracy):
            centre = [circles[j-1][0][0] -circles[j-1][1]*cos(i*(j-1)),circles[j-1][0][1] - circles[j-1][1]*sin(i*(j-1))]
            circles.append([centre,scale*coeffs(j)])
        
        
        screen.fill(white)
        centres=[]
        plotting_circles=[j for j in circles]
        plotting_circles.pop(len(plotting_circles)-1)

        #Plots the circles if they are big enough to be seen
        for j in plotting_circles:
            intcentre = (int(j[0][0]),int(j[0][1]))
            centres.append(intcentre)
            if int(j[1]) >= 2:
                circle(intcentre, int(j[1]), black)
        
        #Decides whether the locii has been drawn already 
        if drawn == False:
            locii.append(circles[len(circles)-1][0])
        #if i*coeffs(1) > 4*period:
            #drawn = True
        
        #Draws the locii
        if len(locii)>1:
            line(locii,grey)

        #Y-axis
        line([(9*display_width//16,display_height//8),(9*display_width//16,7*display_height//8)],black)
        line([(9*display_width//16,display_height//2),(15*display_width//16,display_height//2)],black)
        
        #Shows the 'drawing' line
        line([(circles[len(circles)-1][0][0],circles[len(circles)-1][0][1]),(15*display_width//16,circles[len(circles)-1][0][1])],green)
        
        #adds a new point to the plot
        linepoints.append([15*display_width//16,circles[len(circles)-1][0][1]])

        centres.append([int(circles[len(circles)-1][0][0]),int(circles[len(circles)-1][0][1])])
        #Line showing direction of each sine vector
        line(centres, red)
        
        #Moves each point on the plot left by 1 pixel each frame
        for j in linepoints:
            j[0] -= 1
        
        #If a point on the graph is to the left of the y-axis then the point needs to be removed
        if removing ==False:
            if linepoints[0][0] < 9*display_width//16:
                removing = True
        if removing == True:
            linepoints.pop(0)
        
        #Plots the line represented by the points made by the 'drawing' line
        if len(linepoints) >1:
            line(linepoints, blue)
        
        i+=0.03
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
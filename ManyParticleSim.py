import pygame
import time

pygame.init()

display_width = 1080
display_height = 960

black = (0,0,0)
white = (255,255,255)

def dist(x1,x2):
    return ((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2)**0.5

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Particle Sim')
clock = pygame.time.Clock()

point_density=1
number_points=int(3+47*point_density)
width_partition=display_width//(number_points + 1)
height_partition=display_height//(number_points + 1)
initial_grid=[]
for i in range(1,number_points+1):
    for j in range(1,number_points+1):
        initial_grid.append([i*width_partition,j*height_partition])
points=initial_grid
point_force=[[display_width//2,display_height//2] for i in range(number_points**2)]
point_speed=[[0,0] for i in range(number_points**2)]

centre = [display_width/2, display_height/2]

def game_loop():
    gameExit = False
    dt=0.01
    point_mass=1
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        for i in range(0,len(points)):
            distance = dist(centre,points[i])
            point_force[i][0] = display_width/2 - points[i][0] - sign(points[i][0]-centre[0])*distance
            point_force[i][1] = display_height/2 - points[i][1] - sign(points[i][1]-centre[1])*distance
            point_speed[i][0] += point_force[i][0]/point_mass * dt 
            point_speed[i][1] += point_force[i][1]/point_mass * dt
            points[i][0] += point_speed[i][0] *dt
            points[i][1] += point_speed[i][1] *dt

        gameDisplay.fill(white)
        for i in points:
            pygame.draw.circle(gameDisplay, black, (int(i[0]), int(i[1])),2)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
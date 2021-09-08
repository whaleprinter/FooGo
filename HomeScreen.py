from pygame import *
from AllFunctions import *


##Pygame Settings and Loading the Info Screen Image
res = (879, 540)
screen = pygame.display.set_mode(res)
welcome = pygame.image.load('FooGoHomeScreen.png').convert()
screen.blit(welcome, (0, 0))
pygame.display.update()

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked

        if ev.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the
            # button the game is terminated
            point = pygame.mouse.get_pos()

            ##If the Get Started has been pressed, then the program will execute the Calculator.py module
            if (point[0] > 287 and point[0] < 592) and (point[1] >353 and point[1] < 429):
                exec(open("Calculator.py").read())

            ##If the Info Button has been pressed, then the program will execute the InfoScreen.py module
            if (point[0] > 287 and point[0] < 592) and (point[1] >442 and point[1] < 519):
                exec(open("InfoScreen.py").read())


from pygame import *
from AllFunctions import *

##Pygame Settings and Loading the Info Screen Image
res = (879, 540)
screen = pygame.display.set_mode(res)
infoScreen = pygame.image.load('FooGoInfoScreen.png').convert()
screen.blit(infoScreen, (0, 0))
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

            ##If the Home Button has been pressed, then the program will execute the HomeScreen.py module
            if (point[0] > 17 and point[0] < 89) and (point[1] > 14 and point[1] < 86):
                exec(open("HomeScreen.py").read())

            ##If the Map Button has been pressed, then the program will execute the Calculator.py module
            if (point[0] > 789 and point[0] < 861) and (point[1] > 14 and point[1] < 86):
                exec(open("Calculator.py").read())



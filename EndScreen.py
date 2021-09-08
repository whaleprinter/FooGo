from pygame import *
from main import *

pygame.display.update()

while True:


    for ev in pygame.event.get():



        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pointButton = pygame.mouse.get_pos()
            ##Checks if mouse is pressed on the "Clear Selections" button and Resets the Program Accordingly
            if (pointButton[0] > 10 and pointButton[0] < 55) and (pointButton[1] > 7 and pointButton[1] < 52):
                exec(open("HomeScreen.py").read())
            # If exit button is pressed, then the program will automatically shut down
            elif (pointButton[0] > 824 and pointButton[0] < 869) and (pointButton[1] > 7 and pointButton[1] < 52):
                logOff = pygame.image.load('LogOffScreen.png').convert()
                screen.blit(logOff, (0, 0))
                pygame.display.update()
                tm.sleep(2)
                pygame.quit()
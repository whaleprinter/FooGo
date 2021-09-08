# FooGo--A Smart, Safety-Focused Navigation System
# Authors: Roshan Sundaram and Ajay Dakoriya
# Started: 8/25/2021
# Presentation: 9/8/2021

# To get FooGo to work, simply run the "main.py" file





import pygame
from AllFunctions import *
##https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/



##Initializes pygame for the entire program
pygame.init()
pygame.display.set_caption('FooGo')
##Executes the Home Screen Module
exec(open("HomeScreen.py").read())

# https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
# https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame


# Import all necessary packages
import pygame
from AllFunctions import *
from main import *
from GoogleMaps import *
import time as tm

# Getting Pygame window configured by displaying the USA map and initializing the fonts that we will be using
pygame.font.init()
BLUE = (0, 0, 255)
font = pygame.font.SysFont('Microsoft JhengHei', 24)
res = (800, 495)
usamap = pygame.image.load('FooGoMap.png').convert()
screen.blit(usamap, (0, 0))
pygame.display.update()

# Initializing the Button Press Variables That are used to differentiate between the origin and the destination
pressedOnce = False
buttonPresses = 0

# Initializing the usesWalking and usesFlying variables that will be later mutated in order to indicate whether walking or flying is used or not
usesWalking = False
usesFlying = False

# Starting the Button Press Detector (pygame)
while True:

    # For each mouse movement, pygame will run the statements within the for loop. In essence, this means that
    # the program will always continue to check for an event and execute certain actions once a certain condition has been met
    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()

        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            pointButton = pygame.mouse.get_pos()  # if mouse is clicked, the position of the cursor is recorded
            # Checks if mouse is pressed on the "Clear Selections" button and Resets the Program Accordingly
            if (pointButton[0] > 13 and pointButton[0] < 207) and (pointButton[1] > 422 and pointButton[1] < 472):
                exec(open("Calculator.py").read())

            # Checks if the Home Button has been pressed and executes HomeScreen.py accordingly
            elif (pointButton[0] > 760 and pointButton[0] < 806) and (pointButton[1] > 482 and pointButton[1] < 528):
                exec(open("HomeScreen.py").read())

            # Checks if the Info Button is pressed and executes InfoScreen.py accordingly
            elif (pointButton[0] > 818 and pointButton[0] < 864) and (pointButton[1] > 482 and pointButton[1] < 528):
                exec(open("InfoScreen.py").read())

            # Checks if mouse is pressed on the "Quit Program" Button and shuts down the program accordingly
            elif (pointButton[0] > 13 and pointButton[0] < 207) and (pointButton[1] > 480 and pointButton[1] < 530):
                # Executing the log off sequence, which consists of the log off screen being displayed and the program closing after 2 seconds
                logOff = pygame.image.load('LogOffScreen.png').convert()
                screen.blit(logOff, (0, 0))
                pygame.display.update()
                tm.sleep(2)
                pygame.quit()

            # If none of those buttons are pressed, then program will continue as normal and the origin/destination will be selected
            else:
                # Initializing the lists for coordinates


                # If a point on the map has not yet been selected by the user
                if pressedOnce == False:

                    # Get mouse position and assign the values of x and y to x1 and y1, respectively
                    point1 = pygame.mouse.get_pos()
                    x1 = point1[0]
                    y1 = point1[1]


                    # Calculating nearest airport and highway
                    distance1Test, oriAirport = originAirport(x1, y1)
                    closestOriHighway = originHighway(x1, y1)

                    # Converting coordinates of closest airport and highway from pixels to coordinates
                    latOri, longOri = pixelsToCoordinates(x1, y1)
                    latOriAirport, longOriAirport = pixelsToCoordinates(oriAirport[0], oriAirport[1])
                    latOriHighway, longOriHighway = pixelsToCoordinates(closestOriHighway[0], closestOriHighway[1])

                    # Format the coords_0, coords_1 in the format that the Google Maps API wants
                    coords_0 = str(str(latOri) + "," + str(longOri))
                    coords_1 = str(str(latOriAirport) + "," + str(longOriAirport))
                    coords_2 = str(str(latOriHighway) + "," + str(longOriHighway))

                    # Calling the Google Maps API in order to calculate distances
                    distanceToOriAirport = routeMapper(coords_0, coords_1, "driving")
                    distanceToOriHighway = routeMapper(coords_0, coords_2, "driving")

                    # Testers
                    # print("Test: ", distanceToAirport)
                    # print("Distance to Closest Origin Airport: ", distanceToOriPort, " Origin Airport: ", oriAirport, "\nDistance to Closest Origin Highway: ", distanceToClosestOriHighway, " Origin Highway: ",closestOriHighway)

                    # Update the Button Presses So that the next conditional (elif) statement can be run
                    pressedOnce = True
                    buttonPresses += 1

                    # Update the image displayed on the screen by overlaying a point pin on the origin coordinate
                    originPlot = pygame.image.load('redIcon.png').convert()
                    screen.blit(originPlot, (x1 - 7, y1 - 15))
                    pygame.display.update()


                # If a point has been selected by the user, then this code is executed, as the program knows that the destination needs to be selected
                elif pressedOnce == True and buttonPresses == 1:
                    # Update the "pressedOnce" variable to ensure that this part of the code doesn't keep getting executed
                    pressedOnce = True
                    # Getting the position of the mouse on the second button click and then setting the variables x2 and y2 equal to the x and y positions, respectively
                    point2 = pygame.mouse.get_pos()
                    x2 = point2[0]
                    y2 = point2[1]

                    # Calculating nearest airport and highway
                    distance2Test, destAirport = destinationAirport(x2, y2)
                    closestDestHighway = destinationHighway(x2, y2)

                    # Testers for Testing Purposes:
                    # print("Distance from origin to airport (crow): ", pixelsToMiles(distance1Test))
                    # print("Distance from destination to airport (crow): ", pixelsToMiles(distance2Test))
                    # print("Origin airport: ", oriAirport)
                    # print("Destination airport: ", destAirport)

                    # Converting coordinates of closest airport and highway from pixels to coordinates
                    latDest, longDest = pixelsToCoordinates(x2, y2)
                    latDestAirport, longDestAirport = pixelsToCoordinates(destAirport[0], destAirport[1])
                    latDestHighway, longDestHighway = pixelsToCoordinates(closestDestHighway[0], closestDestHighway[1])

                    # Format the coords_00, coords_01, and coords_02 in the format that the Google Maps API wants
                    # These coordinates are used for the destination and its respective highway and airport
                    coords_00 = str(str(latDest) + "," + str(longDest))
                    coords_01 = str(str(latDestAirport) + "," + str(longDestAirport))
                    coords_02 = str(str(latDestHighway) + "," + str(longDestHighway))

                    # Calling the Google Maps API in order to calculate distances
                    distanceToDestAirport = routeMapper(coords_00, coords_01, "driving")
                    distanceToDestHighway = routeMapper(coords_00, coords_02, "driving")

                    # Driving distance between highway entrance and exit using Google Maps API
                    distanceCarHighway = routeMapper(coords_2, coords_02, "driving")


                    # Calculating the total driving distance between origin and origin airport as well as destination and destination airport
                    drivingDistanceToAirports = metersToMiles(distanceToOriAirport + distanceToDestAirport)

                    # Update button press variables
                    buttonPresses += 1

                    # Display the second red map pin
                    destPlot = pygame.image.load('redIcon.png').convert()
                    screen.blit(destPlot, (x2 - 7, y2 - 15))
                    pygame.display.update()

                    # This logic prints out the driving distance using highways only if the distance between points is greater than 100 miles
                    if metersToMiles(routeMapper(coords_2, coords_02, "driving")) > 350:
                        totalDistanceCar = metersToMiles(distanceToOriHighway) + metersToMiles(distanceCarHighway) + metersToMiles(distanceToDestHighway)
                        safetyOfCarTrip = safetyDriving(totalDistanceCar)
                    else: # Else, the function will use the Google Maps API to simply calculate the distance between points using country/rural roads
                        totalDistanceCar = metersToMiles(routeMapper(coords_0, coords_00, "driving"))
                        safetyOfCarTrip = safetyDriving(totalDistanceCar)

                    # Check to see whether flying is practical or not. If the route is greater than 100 miles, then FooGo will suggest flying.
                    # Otherwise, if the route is shorter than that, FooGo will suggest that the user not fly
                    if (pixelsToMiles(distanceFormula(point1, point2)) > 100) and (oriAirport != destAirport):
                        usesFlying = True
                        totalDistanceFlying = distanceFormula(oriAirport, destAirport)
                        safetyOfPlaneTrip = safetyFlying(drivingDistanceToAirports, totalDistanceFlying)
                    else:
                        usesFlying = False

                    # Determines the distance and safety of walking, if the journey is less than 35 miles
                    if metersToMiles(routeMapper(coords_0, coords_00, "walking")) < 35:
                        usesWalking = True
                        totalDistanceWalking = metersToMiles(routeMapper(coords_0, coords_00, "walking"))
                        safetyOfWalkingTrip = safetyWalking(totalDistanceWalking)

                    # Displays the output screen, which has spaces for driving, flying, and walking
                    outputScreen = pygame.image.load('FooGoOutputScreen.png').convert()
                    screen.blit(outputScreen, (0, 0))
                    pygame.display.update()

                    # Displaying the final values for the car distance and safety
                    carImg = font.render(f'The total distance that the car travels is: {round(totalDistanceCar)} miles.', False, BLUE)
                    carImg2 = font.render(f'The chance of death on this journey would be 1 in {round(safetyOfCarTrip)}.', False, BLUE)
                    screen.blit(carImg, (56, 86))
                    screen.blit(carImg2, (56, 106))

                    # If the system decides that flying is a viable option, then the respective messages are displayed. If not, then system
                    # alerts user that flying is not a practical option.
                    if usesFlying == False:
                        planeImg = font.render(f'Flying is not a good option on this route, as the distances are too short.', False, BLUE)
                        screen.blit(planeImg, (56, 247))
                    elif usesFlying == True:
                        planeImg = font.render(f'The driving distance to the airport is {round(drivingDistanceToAirports)} miles.', False, BLUE)
                        planeImg2 = font.render(f'The total distance that the plane travels is: {round(totalDistanceFlying)} miles.', False, BLUE)
                        planeImg3 = font.render(f'The chance of death on this journey would be 1 in {round(safetyOfPlaneTrip)}.', False, BLUE)
                        screen.blit(planeImg, (56, 247))
                        screen.blit(planeImg2, (56, 267))
                        screen.blit(planeImg3, (56, 287))

                    # If the system decides that walking is a viable option, then the respective messages are displayed. If not, then system
                    # alerts user that walking is not a practical option.
                    if usesWalking == True:
                        walkingImg = font.render(f'The total distance that you will need to walk is: {round(totalDistanceWalking)} miles.', False, BLUE)
                        walkingImg2 = font.render(f'The chance of death on this journey would be 1 in {round(safetyOfWalkingTrip)}.', False, BLUE)
                        walkingImg3 = font.render(f'It will take you approximately {round(walkingSpeed(totalDistanceWalking), 2)} hours to walk this distance.', False, BLUE)

                        screen.blit(walkingImg, (56, 411))
                        screen.blit(walkingImg2, (56, 431))
                        screen.blit(walkingImg3, (56, 451))
                    elif usesWalking == False:
                        walkingImg = font.render(f'Walking is not a good option on this route, as the walking distance is too long!', False, BLUE)
                        screen.blit(walkingImg, (56, 411))

                    ##Returns usesWalking and usesFlying to False, in case anything happens
                    usesWalking = False
                    usesFlying = False

                    # Update the display and execute the EndScreen.py file, which contains the home and exit buttons that can be pressed
                    pygame.display.update()
                    exec(open("EndScreen.py").read())

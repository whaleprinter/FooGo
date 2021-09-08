from numpy import sqrt
from Data import *

##Converts the inputted pixels distance into miles
def pixelsToMiles(pixels):
    return pixels * 3.8 #rough conversion factor between pixels and miles; ~3.8 miles per pixel on the map

##Calculates the amount of time that it will take for a user to walk a certain distance based on the average walking speed of 3-4 miles per hour
def walkingSpeed(miles):
    return miles/3.5

##Converts the inputted meters distance into miles
def metersToMiles(meters):
    return meters/1609 #basic unit conversion between meters and miles

##Calculates pixels to coordinates (latitude and longitude), https://stackoverflow.com/questions/19579818/converting-pixels-to-latlng-coordinates
def pixelsToCoordinates(x, y):
    Long = (0.0692252588 * x) - 126.0575023 ##Conversion formula for x coordinates into longitude
    Lat = (-0.0506782609 * y) + 50.37493913 ##Conversion formula for y coordinates into latitude
    return Lat, Long

##Calculate safety of driving by multiplying the number of miles driven by the fatality rate
def safetyDriving(miles):
    fatalitiesThroughDrivingTrip = miles * (1.37/100000000) ##1.37 deaths per 100,000,000 miles driven, https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813115
    chanceOfDeathCar = 0 #Ensures that program never gives a "divide by zero" error
    if fatalitiesThroughDrivingTrip != 0:
        chanceOfDeathCar = (1 / fatalitiesThroughDrivingTrip)
    return chanceOfDeathCar

##Calculating safety of flying (includes driving to the airport and flying on the plane itself)
def safetyFlying(milesDriven, milesFlown):
    fatalitiesThroughFlyingTrip = milesFlown * (0.2/10000000000) ##0.2 deaths per 10,000,000,000 miles flown, https://www.bts.gov/archive/publications/transportation_statistics_annual_report/2015/tables/ch6/table6_1, https://www.bts.gov/content/us-passenger-miles
    fatalitiesThroughDrivingAirport = milesDriven * (1.37 / 100000000)  ##1.37 deaths per 100,000,000 miles driven, https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/813115
    chanceOfDeathPlane = 0 #Ensures that program never gives a "divide by zero" error
    if fatalitiesThroughFlyingTrip != 0:
        chanceOfDeathPlane = (1 / (fatalitiesThroughFlyingTrip + fatalitiesThroughDrivingAirport))
    return chanceOfDeathPlane

##Calculating the safety of walking
def safetyWalking(miles):
    fatalitiesThroughWalkingTrip = miles * (1.71/1000000000) ##1.71 deaths per 1,000,000,000 miles flown, https://injuryprevention.bmj.com/content/11/4/232
    chanceOfDeathWalk = 0 #Ensures that program never gives a "divide by zero" error
    if fatalitiesThroughWalkingTrip != 0:
        chanceOfDeathWalk = (1 / fatalitiesThroughWalkingTrip)
    return chanceOfDeathWalk

##Finds the airport closest to the origin
def originAirport(x1, y1):
    DTList = []
    Origin = [x1, y1]

    ##calculates the distances between all airports and the origin
    DTList.append(sqrt(((GSO[1] - Origin[1]) ** 2) + ((GSO[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((RDU[1] - Origin[1]) ** 2) + ((RDU[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((MIA[1] - Origin[1]) ** 2) + ((MIA[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((LAX[1] - Origin[1]) ** 2) + ((LAX[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((ORD[1] - Origin[1]) ** 2) + ((ORD[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((CLT[1] - Origin[1]) ** 2) + ((CLT[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((IAD[1] - Origin[1]) ** 2) + ((IAD[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((SEA[1] - Origin[1]) ** 2) + ((SEA[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((SFO[1] - Origin[1]) ** 2) + ((SFO[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((BOS[1] - Origin[1]) ** 2) + ((BOS[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((PHL[1] - Origin[1]) ** 2) + ((PHL[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((ATL[1] - Origin[1]) ** 2) + ((ATL[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((DFW[1] - Origin[1]) ** 2) + ((DFW[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((IAH[1] - Origin[1]) ** 2) + ((IAH[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((LAS[1] - Origin[1]) ** 2) + ((LAS[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((DEN[1] - Origin[1]) ** 2) + ((DEN[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((PHX[1] - Origin[1]) ** 2) + ((PHX[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((EWR[1] - Origin[1]) ** 2) + ((EWR[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((DCA[1] - Origin[1]) ** 2) + ((DCA[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((TPA[1] - Origin[1]) ** 2) + ((TPA[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((DTW[1] - Origin[1]) ** 2) + ((DTW[0] - Origin[0]) ** 2)))
    DTList.append(sqrt(((SLC[1] - Origin[1]) ** 2) + ((SLC[0] - Origin[0]) ** 2)))

    ##find the minimum distance
    minValue = min(DTList)
    index = DTList.index(minValue)  ##https://pythonexamples.org/python-find-index-of-item-in-list/
    ##sets the closest airport's coordinates as the returned coordinates
    airportO = []
    if index == 0:
        airportO = GSO.copy()
    elif index == 1:
        airportO = RDU.copy()
    elif index == 2:
        airportO = MIA.copy()
    elif index == 3:
        airportO = LAX.copy()
    elif index == 4:
        airportO = ORD.copy()
    elif index == 5:
        airportO = CLT.copy()
    elif index == 6:
        airportO = IAD.copy()
    elif index == 7:
        airportO = SEA.copy()
    elif index == 8:
        airportO = SFO.copy()
    elif index == 9:
        airportO = BOS.copy()
    elif index == 10:
        airportO = PHL.copy()
    elif index == 11:
        airportO = ATL.copy()
    elif index == 12:
        airportO = DFW.copy()
    elif index == 13:
        airportO = IAH.copy()
    elif index == 14:
        airportO = LAS.copy()
    elif index == 15:
        airportO = DEN.copy()
    elif index == 16:
        airportO = PHX.copy()
    elif index == 17:
        airportO = EWR.copy()
    elif index == 18:
        airportO = DCA.copy()
    elif index == 19:
        airportO = TPA.copy()
    elif index == 20:
        airportO = DTW.copy()
    elif index == 21:
        airportO = SLC.copy()

    return minValue, airportO

##Finds the closest airport to the destination
def destinationAirport(x2, y2):
    DFList = []
    Destination = [x2, y2]
    ##calculates the distances between all airports and the origin
    DFList.append(sqrt(((GSO[1] - Destination[1]) ** 2) + ((GSO[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((RDU[1] - Destination[1]) ** 2) + ((RDU[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((MIA[1] - Destination[1]) ** 2) + ((MIA[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((LAX[1] - Destination[1]) ** 2) + ((LAX[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((ORD[1] - Destination[1]) ** 2) + ((ORD[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((CLT[1] - Destination[1]) ** 2) + ((CLT[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((IAD[1] - Destination[1]) ** 2) + ((IAD[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((SEA[1] - Destination[1]) ** 2) + ((SEA[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((SFO[1] - Destination[1]) ** 2) + ((SFO[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((BOS[1] - Destination[1]) ** 2) + ((BOS[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((PHL[1] - Destination[1]) ** 2) + ((PHL[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((ATL[1] - Destination[1]) ** 2) + ((ATL[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((DFW[1] - Destination[1]) ** 2) + ((DFW[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((IAH[1] - Destination[1]) ** 2) + ((IAH[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((LAS[1] - Destination[1]) ** 2) + ((LAS[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((DEN[1] - Destination[1]) ** 2) + ((DEN[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((PHX[1] - Destination[1]) ** 2) + ((PHX[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((EWR[1] - Destination[1]) ** 2) + ((EWR[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((DCA[1] - Destination[1]) ** 2) + ((DCA[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((TPA[1] - Destination[1]) ** 2) + ((TPA[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((DTW[1] - Destination[1]) ** 2) + ((DTW[0] - Destination[0]) ** 2)))
    DFList.append(sqrt(((SLC[1] - Destination[1]) ** 2) + ((SLC[0] - Destination[0]) ** 2)))

    ##find the minimum distance
    minValue2 = min(DFList)
    index2 = DFList.index(minValue2)  ##https://pythonexamples.org/python-find-index-of-item-in-list/

    ##sets the closest airport's coordinates as the returned coordinates
    if index2 == 0:
        airportD = GSO.copy()
    elif index2 == 1:
        airportD = RDU.copy()
    elif index2 == 2:
        airportD = MIA.copy()
    elif index2 == 3:
        airportD = LAX.copy()
    elif index2 == 4:
        airportD = ORD.copy()
    elif index2 == 5:
        airportD = CLT.copy()
    elif index2 == 6:
        airportD = IAD.copy()
    elif index2 == 7:
        airportD = SEA.copy()
    elif index2 == 8:
        airportD = SFO.copy()
    elif index2 == 9:
        airportD = BOS.copy()
    elif index2 == 10:
        airportD = PHL.copy()
    elif index2 == 11:
        airportD = ATL.copy()
    elif index2 == 12:
        airportD = DFW.copy()
    elif index2 == 13:
        airportD = IAH.copy()
    elif index2 == 14:
        airportD = LAS.copy()
    elif index2 == 15:
        airportD = DEN.copy()
    elif index2 == 16:
        airportD = PHX.copy()
    elif index2 == 17:
        airportD = EWR.copy()
    elif index2 == 18:
        airportD = DCA.copy()
    elif index2 == 19:
        airportD = TPA.copy()
    elif index2 == 20:
        airportD = DTW.copy()
    elif index2 == 21:
        airportD = SLC.copy()

    return minValue2, airportD


##finds the distance that the plane has to travel (distance between selected airports)
def distanceFormula(origin, destination):
    x1a = origin[0]
    y1a = origin[1]
    x2a = destination[0]
    y2a = destination[1]
    return pixelsToMiles((sqrt(((y2a - y1a) ** 2) + ((x2a - x1a) ** 2)))) #Basic distance formula calculator

##Finds the closest highway to the origin
def originHighway(x1, y1):
    Origin = [x1, y1]
    IOList = []
    ##Interstate 5
    IOList.append(sqrt(((FiveSanDiego[1] - Origin[1]) ** 2) + ((FiveSanDiego[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiveLA[1] - Origin[1]) ** 2) + ((FiveLA[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiveSacramento[1] - Origin[1]) ** 2) + ((FiveSacramento[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiveBorder[1] - Origin[1]) ** 2) + ((FiveBorder[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiveGrantsPass[1] - Origin[1]) ** 2) + ((FiveGrantsPass[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FivePortland[1] - Origin[1]) ** 2) + ((FivePortland[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiveSeattle[1] - Origin[1]) ** 2) + ((FiveSeattle[0] - Origin[0]) ** 2)))

    ##Interstate 15
    IOList.append(sqrt(((FifteenSanDiego[1] - Origin[1]) ** 2) + ((FifteenSanDiego[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FifteenBarstow[1] - Origin[1]) ** 2) + ((FifteenBarstow[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FifteenVegas[1] - Origin[1]) ** 2) + ((FifteenVegas[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FifteenStGeorge[1] - Origin[1]) ** 2) + ((FifteenStGeorge[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FifteenSLC[1] - Origin[1]) ** 2) + ((FifteenSLC[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FifteenPocatello[1] - Origin[1]) ** 2) + ((FifteenPocatello[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FifteenBorder[1] - Origin[1]) ** 2) + ((FifteenBorder[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FifteenHelena[1] - Origin[1]) ** 2) + ((FifteenHelena[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FifteenCanada[1] - Origin[1]) ** 2) + ((FifteenCanada[0] - Origin[0]) ** 2)))

    ##Interstate 25
    IOList.append(sqrt(((TwentyFiveElPaso[1] - Origin[1]) ** 2) + ((TwentyFiveElPaso[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((TwentyFiveLasCruces[1] - Origin[1]) ** 2) + ((TwentyFiveLasCruces[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((TwentyFiveAlbuqurque[1] - Origin[1]) ** 2) + ((TwentyFiveAlbuqurque[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((TwentyFiveBorder[1] - Origin[1]) ** 2) + ((TwentyFiveBorder[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((TwentyFiveCheyenne[1] - Origin[1]) ** 2) + ((TwentyFiveCheyenne[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((TwentyFiveCasper[1] - Origin[1]) ** 2) + ((TwentyFiveCasper[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((TwentyFiveSheridan[1] - Origin[1]) ** 2) + ((TwentyFiveSheridan[0] - Origin[0]) ** 2)))

    ##Interstate 35
    IOList.append(sqrt(((ThirtyFiveLaredo[1] - Origin[1]) ** 2) + ((ThirtyFiveLaredo[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((ThirtyFiveSanAntonio[1] - Origin[1]) ** 2) + ((ThirtyFiveSanAntonio[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((ThirtyFiveDallas[1] - Origin[1]) ** 2) + ((ThirtyFiveDallas[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((ThirtyFiveOklahomaCity[1] - Origin[1]) ** 2) + ((ThirtyFiveOklahomaCity[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((ThirtyFiveWichita[1] - Origin[1]) ** 2) + ((ThirtyFiveWichita[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((ThirtyFiveKansasCity[1] - Origin[1]) ** 2) + ((ThirtyFiveKansasCity[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((ThirtyFiveDesMoines[1] - Origin[1]) ** 2) + ((ThirtyFiveDesMoines[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((ThirtyFiveAlbertLea[1] - Origin[1]) ** 2) + ((ThirtyFiveAlbertLea[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((ThirtyFiveMinneapolis[1] - Origin[1]) ** 2) + ((ThirtyFiveMinneapolis[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((ThirtyFiveDuluth[1] - Origin[1]) ** 2) + ((ThirtyFiveDuluth[0] - Origin[0]) ** 2)))

    ##Interstate 55
    IOList.append(sqrt(((FiftyFiveNewOrleans[1] - Origin[1]) ** 2) + ((FiftyFiveNewOrleans[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveHammond[1] - Origin[1]) ** 2) + ((FiftyFiveHammond[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveJackson[1] - Origin[1]) ** 2) + ((FiftyFiveJackson[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveBatesville[1] - Origin[1]) ** 2) + ((FiftyFiveBatesville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveMemphis[1] - Origin[1]) ** 2) + ((FiftyFiveMemphis[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveScottCity[1] - Origin[1]) ** 2) + ((FiftyFiveScottCity[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveBloomsdale[1] - Origin[1]) ** 2) + ((FiftyFiveBloomsdale[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveStLouis[1] - Origin[1]) ** 2) + ((FiftyFiveStLouis[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveMtOlive[1] - Origin[1]) ** 2) + ((FiftyFiveMtOlive[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveSpringfield[1] - Origin[1]) ** 2) + ((FiftyFiveSpringfield[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveBloomington[1] - Origin[1]) ** 2) + ((FiftyFiveBloomington[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveDwight[1] - Origin[1]) ** 2) + ((FiftyFiveDwight[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveBolingbrook[1] - Origin[1]) ** 2) + ((FiftyFiveBolingbrook[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FiftyFiveChicago[1] - Origin[1]) ** 2) + ((FiftyFiveChicago[0] - Origin[0]) ** 2)))

    ##Interstate 65
    IOList.append(sqrt(((SixtyFiveMobile[1] - Origin[1]) ** 2) + ((SixtyFiveMobile[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveGreenville[1] - Origin[1]) ** 2) + ((SixtyFiveGreenville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveMontgomery[1] - Origin[1]) ** 2) + ((SixtyFiveMontgomery[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveDecatur[1] - Origin[1]) ** 2) + ((SixtyFiveDecatur[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveFrankewing[1] - Origin[1]) ** 2) + ((SixtyFiveFrankewing[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveNashville[1] - Origin[1]) ** 2) + ((SixtyFiveNashville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveBowlingGreen[1] - Origin[1]) ** 2) + ((SixtyFiveBowlingGreen[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveElizabethtown[1] - Origin[1]) ** 2) + ((SixtyFiveElizabethtown[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveLouisville[1] - Origin[1]) ** 2) + ((SixtyFiveLouisville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveScottsburg[1] - Origin[1]) ** 2) + ((SixtyFiveScottsburg[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveColumbus[1] - Origin[1]) ** 2) + ((SixtyFiveColumbus[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveIndianapolis[1] - Origin[1]) ** 2) + ((SixtyFiveIndianapolis[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveLafayette[1] - Origin[1]) ** 2) + ((SixtyFiveLafayette[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveRemington[1] - Origin[1]) ** 2) + ((SixtyFiveRemington[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SixtyFiveGary[1] - Origin[1]) ** 2) + ((SixtyFiveGary[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFourChicago[1] - Origin[1]) ** 2) + ((NinetyFourChicago[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFourBorder[1] - Origin[1]) ** 2) + ((NinetyFourBorder[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyOneMtPleasant[1] - Origin[1]) ** 2) + ((FortyOneMtPleasant[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyOneMilwaukee[1] - Origin[1]) ** 2) + ((FortyOneMilwaukee[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyThreeSheboygan[1] - Origin[1]) ** 2) + ((FortyThreeSheboygan[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyThreeGreenBay[1] - Origin[1]) ** 2) + ((FortyThreeGreenBay[0] - Origin[0]) ** 2)))

    ##Interstate 75
    IOList.append(sqrt(((SeventyFiveMiami[1] - Origin[1]) ** 2) + ((SeventyFiveMiami[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveFortMyers[1] - Origin[1]) ** 2) + ((SeventyFiveFortMyers[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFivePortCharlotte[1] - Origin[1]) ** 2) + ((SeventyFivePortCharlotte[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveTampa[1] - Origin[1]) ** 2) + ((SeventyFiveTampa[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveOcala[1] - Origin[1]) ** 2) + ((SeventyFiveOcala[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveGainesville[1] - Origin[1]) ** 2) + ((SeventyFiveGainesville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveValdosta[1] - Origin[1]) ** 2) + ((SeventyFiveValdosta[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveTifton[1] - Origin[1]) ** 2) + ((SeventyFiveTifton[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveVienna[1] - Origin[1]) ** 2) + ((SeventyFiveVienna[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFivePerry[1] - Origin[1]) ** 2) + ((SeventyFivePerry[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveMacon[1] - Origin[1]) ** 2) + ((SeventyFiveMacon[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveAtlanta[1] - Origin[1]) ** 2) + ((SeventyFiveAtlanta[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveCalhoun[1] - Origin[1]) ** 2) + ((SeventyFiveCalhoun[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveChattanooga[1] - Origin[1]) ** 2) + ((SeventyFiveChattanooga[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveKnoxville[1] - Origin[1]) ** 2) + ((SeventyFiveKnoxville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveLondon[1] - Origin[1]) ** 2) + ((FortyThreeGreenBay[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveLexington[1] - Origin[1]) ** 2) + ((SeventyFiveLexington[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveCincinnati[1] - Origin[1]) ** 2) + ((SeventyFiveCincinnati[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveDayton[1] - Origin[1]) ** 2) + ((SeventyFiveDayton[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveWapakoneta[1] - Origin[1]) ** 2) + ((SeventyFiveWapakoneta[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveBeaverdam[1] - Origin[1]) ** 2) + ((SeventyFiveBeaverdam[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveToledo[1] - Origin[1]) ** 2) + ((SeventyFiveToledo[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveMonroe[1] - Origin[1]) ** 2) + ((SeventyFiveMonroe[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFivePontiac[1] - Origin[1]) ** 2) + ((SeventyFivePontiac[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((SeventyFiveFlint[1] - Origin[1]) ** 2) + ((SeventyFiveFlint[0] - Origin[0]) ** 2)))

    ##Interstate 95
    IOList.append(sqrt(((NinetyFiveMiami[1] - Origin[1]) ** 2) + ((NinetyFiveMiami[0] - Origin[0]) ** 2)))
    IOList.append(
        sqrt(((NinetyFiveWestPalmBeach[1] - Origin[1]) ** 2) + ((NinetyFiveWestPalmBeach[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveDaytonaBeach[1] - Origin[1]) ** 2) + ((NinetyFiveDaytonaBeach[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveStAugustine[1] - Origin[1]) ** 2) + ((NinetyFiveStAugustine[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveJacksonville[1] - Origin[1]) ** 2) + ((NinetyFiveJacksonville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveSavannah[1] - Origin[1]) ** 2) + ((NinetyFiveSavannah[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveRosinville[1] - Origin[1]) ** 2) + ((NinetyFiveRosinville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveFlorence[1] - Origin[1]) ** 2) + ((NinetyFiveFlorence[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveLumberton[1] - Origin[1]) ** 2) + ((NinetyFiveLumberton[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveFayetteville[1] - Origin[1]) ** 2) + ((NinetyFiveFayetteville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveSmithfield[1] - Origin[1]) ** 2) + ((NinetyFiveSmithfield[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveEmporia[1] - Origin[1]) ** 2) + ((NinetyFiveEmporia[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveRichmond[1] - Origin[1]) ** 2) + ((NinetyFiveRichmond[0] - Origin[0]) ** 2)))
    IOList.append(
        sqrt(((NinetyFiveFredericksburg[1] - Origin[1]) ** 2) + ((NinetyFiveFredericksburg[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveWashington[1] - Origin[1]) ** 2) + ((NinetyFiveWashington[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveWilmington[1] - Origin[1]) ** 2) + ((NinetyFiveWilmington[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFivePhiladelphia[1] - Origin[1]) ** 2) + ((NinetyFivePhiladelphia[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveNewark[1] - Origin[1]) ** 2) + ((NinetyFiveNewark[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveStamford[1] - Origin[1]) ** 2) + ((NinetyFiveStamford[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveBridgeport[1] - Origin[1]) ** 2) + ((NinetyFiveBridgeport[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveNewHaven[1] - Origin[1]) ** 2) + ((NinetyFiveNewHaven[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveProvidence[1] - Origin[1]) ** 2) + ((NinetyFiveProvidence[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveBoston[1] - Origin[1]) ** 2) + ((NinetyFiveBoston[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFivePortsmouth[1] - Origin[1]) ** 2) + ((NinetyFivePortsmouth[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveBangor[1] - Origin[1]) ** 2) + ((NinetyFiveBangor[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((NinetyFiveBorder[1] - Origin[1]) ** 2) + ((NinetyFiveBorder[0] - Origin[0]) ** 2)))

    ##Interstate 40
    IOList.append(sqrt(((FortyBarstow[1] - Origin[1]) ** 2) + ((FortyBarstow[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyKingman[1] - Origin[1]) ** 2) + ((FortyKingman[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyFlagstaff[1] - Origin[1]) ** 2) + ((FortyFlagstaff[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyGallup[1] - Origin[1]) ** 2) + ((FortyGallup[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyAlbuquerque[1] - Origin[1]) ** 2) + ((FortyAlbuquerque[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyAmarillo[1] - Origin[1]) ** 2) + ((FortyAmarillo[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyOklahomaCity[1] - Origin[1]) ** 2) + ((FortyOklahomaCity[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyLittleRock[1] - Origin[1]) ** 2) + ((FortyLittleRock[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyMemphis[1] - Origin[1]) ** 2) + ((FortyMemphis[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyNashville[1] - Origin[1]) ** 2) + ((FortyNashville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyAsheville[1] - Origin[1]) ** 2) + ((FortyAsheville[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyHickory[1] - Origin[1]) ** 2) + ((FortyHickory[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyWinstonSalem[1] - Origin[1]) ** 2) + ((FortyWinstonSalem[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyGreensboro[1] - Origin[1]) ** 2) + ((FortyGreensboro[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyBurlington[1] - Origin[1]) ** 2) + ((FortyBurlington[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyRaleighDurham[1] - Origin[1]) ** 2) + ((FortyRaleighDurham[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyBenson[1] - Origin[1]) ** 2) + ((FortyBenson[0] - Origin[0]) ** 2)))
    IOList.append(sqrt(((FortyWilmington[1] - Origin[1]) ** 2) + ((FortyWilmington[0] - Origin[0]) ** 2)))

    minValueHighwayOrigin = min(IOList)
    indexValueHighwayOrigin = IOList.index(
        minValueHighwayOrigin)  ##https://pythonexamples.org/python-find-index-of-item-in-list/

    highwayO = []
    if indexValueHighwayOrigin == 0:  ##five
        highwayO = FiveSanDiego.copy()
    elif indexValueHighwayOrigin == 1:
        highwayO = FiveLA.copy()
    elif indexValueHighwayOrigin == 2:
        highwayO = FiveSacramento.copy()
    elif indexValueHighwayOrigin == 3:
        highwayO = FiveBorder.copy()
    elif indexValueHighwayOrigin == 4:
        highwayO = FiveGrantsPass.copy()
    elif indexValueHighwayOrigin == 5:
        highwayO = FivePortland.copy()
    elif indexValueHighwayOrigin == 6:
        highwayO = FiveSeattle.copy()
    elif indexValueHighwayOrigin == 7:  ##fifteen
        highwayO = FifteenSanDiego.copy()
    elif indexValueHighwayOrigin == 8:
        highwayO = FifteenBarstow.copy()
    elif indexValueHighwayOrigin == 9:
        highwayO = FifteenVegas.copy()
    elif indexValueHighwayOrigin == 10:
        highwayO = FifteenStGeorge.copy()
    elif indexValueHighwayOrigin == 11:
        highwayO = FifteenSLC.copy()
    elif indexValueHighwayOrigin == 12:
        highwayO = FifteenPocatello.copy()
    elif indexValueHighwayOrigin == 13:
        highwayO = FifteenBorder.copy()
    elif indexValueHighwayOrigin == 14:
        highwayO = FifteenHelena.copy()
    elif indexValueHighwayOrigin == 15:
        highwayO = FifteenCanada.copy()
    elif indexValueHighwayOrigin == 16:  ##twenty five
        highwayO = TwentyFiveElPaso.copy()
    elif indexValueHighwayOrigin == 17:
        highwayO = TwentyFiveLasCruces.copy()
    elif indexValueHighwayOrigin == 18:
        highwayO = TwentyFiveAlbuqurque.copy()
    elif indexValueHighwayOrigin == 19:
        highwayO = TwentyFiveCheyenne.copy()
    elif indexValueHighwayOrigin == 20:
        highwayO = TwentyFiveCasper.copy()
    elif indexValueHighwayOrigin == 21:
        highwayO = TwentyFiveSheridan.copy()
    elif indexValueHighwayOrigin == 22:  ##thirty five
        highwayO = ThirtyFiveLaredo.copy()
    elif indexValueHighwayOrigin == 23:
        highwayO = ThirtyFiveSanAntonio.copy()
    elif indexValueHighwayOrigin == 24:
        highwayO = ThirtyFiveDallas.copy()
    elif indexValueHighwayOrigin == 25:
        highwayO = ThirtyFiveOklahomaCity.copy()
    elif indexValueHighwayOrigin == 26:
        highwayO = ThirtyFiveWichita.copy()
    elif indexValueHighwayOrigin == 27:
        highwayO = ThirtyFiveKansasCity.copy()
    elif indexValueHighwayOrigin == 28:
        highwayO = ThirtyFiveDesMoines.copy()
    elif indexValueHighwayOrigin == 29:
        highwayO = ThirtyFiveAlbertLea.copy()
    elif indexValueHighwayOrigin == 30:
        highwayO = ThirtyFiveMinneapolis.copy()
    elif indexValueHighwayOrigin == 31:
        highwayO = ThirtyFiveDuluth.copy()
    elif indexValueHighwayOrigin == 32:  ##fifty five
        highwayO = FiftyFiveNewOrleans.copy()
    elif indexValueHighwayOrigin == 33:
        highwayO = FiftyFiveHammond.copy()
    elif indexValueHighwayOrigin == 34:
        highwayO = FiftyFiveJackson.copy()
    elif indexValueHighwayOrigin == 35:
        highwayO = FiftyFiveBatesville.copy()
    elif indexValueHighwayOrigin == 36:
        highwayO = FiftyFiveMemphis.copy()
    elif indexValueHighwayOrigin == 37:
        highwayO = FiftyFiveScottCity.copy()
    elif indexValueHighwayOrigin == 38:
        highwayO = FiftyFiveBloomsdale.copy()
    elif indexValueHighwayOrigin == 39:
        highwayO = FiftyFiveStLouis.copy()
    elif indexValueHighwayOrigin == 40:
        highwayO = FiftyFiveMtOlive.copy()
    elif indexValueHighwayOrigin == 41:
        highwayO = FiftyFiveSpringfield.copy()
    elif indexValueHighwayOrigin == 42:
        highwayO = FiftyFiveBloomington.copy()
    elif indexValueHighwayOrigin == 43:
        highwayO = FiftyFiveDwight.copy()
    elif indexValueHighwayOrigin == 44:
        highwayO = FiftyFiveBolingbrook.copy()
    elif indexValueHighwayOrigin == 45:
        highwayO = FiftyFiveChicago.copy()
    elif indexValueHighwayOrigin == 46:  ##sixty five
        highwayO = SixtyFiveMobile.copy()
    elif indexValueHighwayOrigin == 47:
        highwayO = SixtyFiveGreenville.copy()
    elif indexValueHighwayOrigin == 48:
        highwayO = SixtyFiveMontgomery.copy()
    elif indexValueHighwayOrigin == 49:
        highwayO = SixtyFiveDecatur.copy()
    elif indexValueHighwayOrigin == 50:
        highwayO = SixtyFiveFrankewing.copy()
    elif indexValueHighwayOrigin == 51:
        highwayO = SixtyFiveNashville.copy()
    elif indexValueHighwayOrigin == 52:
        highwayO = SixtyFiveBowlingGreen.copy()
    elif indexValueHighwayOrigin == 53:
        highwayO = SixtyFiveElizabethtown.copy()
    elif indexValueHighwayOrigin == 54:
        highwayO = SixtyFiveLouisville.copy()
    elif indexValueHighwayOrigin == 55:
        highwayO = SixtyFiveScottsburg.copy()
    elif indexValueHighwayOrigin == 56:
        highwayO = SixtyFiveColumbus.copy()
    elif indexValueHighwayOrigin == 57:
        highwayO = SixtyFiveIndianapolis.copy()
    elif indexValueHighwayOrigin == 58:
        highwayO = SixtyFiveLafayette.copy()
    elif indexValueHighwayOrigin == 59:
        highwayO = SixtyFiveRemington.copy()
    elif indexValueHighwayOrigin == 60:
        highwayO = SixtyFiveGary.copy()
    elif indexValueHighwayOrigin == 61:
        highwayO = NinetyFourChicago.copy()
    elif indexValueHighwayOrigin == 62:
        highwayO = NinetyFourBorder.copy()
    elif indexValueHighwayOrigin == 63:
        highwayO = FortyOneMtPleasant.copy()
    elif indexValueHighwayOrigin == 64:
        highwayO = FortyOneMilwaukee.copy()
    elif indexValueHighwayOrigin == 65:
        highwayO = FortyThreeSheboygan.copy()
    elif indexValueHighwayOrigin == 66:
        highwayO = FortyThreeGreenBay.copy()
    elif indexValueHighwayOrigin == 67:  ##seventy five
        highwayO = SeventyFiveMiami.copy()
    elif indexValueHighwayOrigin == 68:
        highwayO = SeventyFiveFortMyers.copy()
    elif indexValueHighwayOrigin == 69:
        highwayO = SeventyFivePortCharlotte.copy()
    elif indexValueHighwayOrigin == 70:
        highwayO = SeventyFiveTampa.copy()
    elif indexValueHighwayOrigin == 71:
        highwayO = SeventyFiveOcala.copy()
    elif indexValueHighwayOrigin == 72:
        highwayO = SeventyFiveGainesville.copy()
    elif indexValueHighwayOrigin == 73:
        highwayO = SeventyFiveValdosta.copy()
    elif indexValueHighwayOrigin == 74:
        highwayO = SeventyFiveTifton.copy()
    elif indexValueHighwayOrigin == 75:
        highwayO = SeventyFiveVienna.copy()
    elif indexValueHighwayOrigin == 76:
        highwayO = SeventyFivePerry.copy()
    elif indexValueHighwayOrigin == 77:
        highwayOD = SeventyFiveMacon.copy()
    elif indexValueHighwayOrigin == 78:
        highwayO = SeventyFiveAtlanta.copy()
    elif indexValueHighwayOrigin == 79:
        highwayO = SeventyFiveCalhoun.copy()
    elif indexValueHighwayOrigin == 80:
        highwayO = SeventyFiveChattanooga.copy()
    elif indexValueHighwayOrigin == 81:
        highwayO = SeventyFiveKnoxville.copy()
    elif indexValueHighwayOrigin == 82:
        highwayO = SeventyFiveLondon.copy()
    elif indexValueHighwayOrigin == 83:
        highwayO = SeventyFiveLexington.copy()
    elif indexValueHighwayOrigin == 84:
        highwayO = SeventyFiveCincinnati.copy()
    elif indexValueHighwayOrigin == 85:
        highwayO = SeventyFiveDayton.copy()
    elif indexValueHighwayOrigin == 86:
        highwayO = SeventyFiveWapakoneta.copy()
    elif indexValueHighwayOrigin == 87:
        highwayO = SeventyFiveBeaverdam.copy()
    elif indexValueHighwayOrigin == 88:
        highwayO = SeventyFiveToledo.copy()
    elif indexValueHighwayOrigin == 89:
        highwayO = SeventyFiveMonroe.copy()
    elif indexValueHighwayOrigin == 90:
        highwayO = SeventyFivePontiac.copy()
    elif indexValueHighwayOrigin == 91:
        highwayO = SeventyFiveFlint.copy()
    elif indexValueHighwayOrigin == 92:  ##ninety five
        highwayO = NinetyFiveMiami.copy()
    elif indexValueHighwayOrigin == 93:
        highwayO = NinetyFiveWestPalmBeach.copy()
    elif indexValueHighwayOrigin == 94:
        highwayO = NinetyFiveDaytonaBeach.copy()
    elif indexValueHighwayOrigin == 95:
        highwayO = NinetyFiveStAugustine.copy()
    elif indexValueHighwayOrigin == 96:
        highwayO = NinetyFiveJacksonville.copy()
    elif indexValueHighwayOrigin == 97:
        highwayO = NinetyFiveSavannah.copy()
    elif indexValueHighwayOrigin == 98:
        highwayO = NinetyFiveRosinville.copy()
    elif indexValueHighwayOrigin == 99:
        highwayO = NinetyFiveFlorence.copy()
    elif indexValueHighwayOrigin == 100:
        highwayO = NinetyFiveFlorence.copy()
    elif indexValueHighwayOrigin == 101:
        highwayO = NinetyFiveLumberton.copy()
    elif indexValueHighwayOrigin == 102:
        highwayO = NinetyFiveFayetteville.copy()
    elif indexValueHighwayOrigin == 103:
        highwayO = NinetyFiveSmithfield.copy()
    elif indexValueHighwayOrigin == 104:
        highwayO = NinetyFiveEmporia.copy()
    elif indexValueHighwayOrigin == 105:
        highwayO = NinetyFiveRichmond.copy()
    elif indexValueHighwayOrigin == 106:
        highwayO = NinetyFiveFredericksburg.copy()
    elif indexValueHighwayOrigin == 107:
        highwayO = NinetyFiveWashington.copy()
    elif indexValueHighwayOrigin == 108:
        highwayO = NinetyFiveWilmington.copy()
    elif indexValueHighwayOrigin == 109:
        highwayO = NinetyFivePhiladelphia.copy()
    elif indexValueHighwayOrigin == 110:
        highwayO = NinetyFiveNewark.copy()
    elif indexValueHighwayOrigin == 111:
        highwayO = NinetyFiveStamford.copy()
    elif indexValueHighwayOrigin == 112:
        highwayO = NinetyFiveBridgeport.copy()
    elif indexValueHighwayOrigin == 113:
        highwayO = NinetyFiveNewHaven.copy()
    elif indexValueHighwayOrigin == 114:
        highwayO = NinetyFiveProvidence.copy()
    elif indexValueHighwayOrigin == 115:
        highwayO = NinetyFiveBoston.copy()
    elif indexValueHighwayOrigin == 116:
        highwayO = NinetyFivePortsmouth.copy()
    elif indexValueHighwayOrigin == 117:
        highwayO = NinetyFiveBangor.copy()
    elif indexValueHighwayOrigin == 118:
        highwayO = NinetyFiveBorder.copy()
    elif indexValueHighwayOrigin == 119:  ##forty
        highwayO = FortyBarstow.copy()
    elif indexValueHighwayOrigin == 120:
        highwayO = FortyKingman.copy()
    elif indexValueHighwayOrigin == 121:
        highwayO = FortyFlagstaff.copy()
    elif indexValueHighwayOrigin == 122:
        highwayO = FortyGallup.copy()
    elif indexValueHighwayOrigin == 123:
        highwayO = FortyAlbuquerque.copy()
    elif indexValueHighwayOrigin == 124:
        highwayO = FortyAmarillo.copy()
    elif indexValueHighwayOrigin == 125:
        highwayO = FortyOklahomaCity.copy()
    elif indexValueHighwayOrigin == 126:
        highwayO = FortyLittleRock.copy()
    elif indexValueHighwayOrigin == 127:
        highwayO = FortyMemphis.copy()
    elif indexValueHighwayOrigin == 128:
        highwayO = FortyNashville.copy()
    elif indexValueHighwayOrigin == 129:
        highwayO = FortyAsheville.copy()
    elif indexValueHighwayOrigin == 130:
        highwayO = FortyHickory.copy()
    elif indexValueHighwayOrigin == 131:
        highwayO = FortyWinstonSalem.copy()
    elif indexValueHighwayOrigin == 132:
        highwayO = FortyGreensboro.copy()
    elif indexValueHighwayOrigin == 133:
        highwayO = FortyBurlington.copy()
    elif indexValueHighwayOrigin == 134:
        highwayO = FortyRaleighDurham.copy()
    elif indexValueHighwayOrigin == 135:
        highwayO = FortyBenson.copy()
    elif indexValueHighwayOrigin == 136:
        highwayO = FortyWilmington.copy()

    return highwayO

##Finds the closest highway to the destination
def destinationHighway(x2, y2):
    Destination = [x2, y2]
    IDList = []
    ##Interstate 5
    IDList.append(sqrt(((FiveSanDiego[1] - Destination[1]) ** 2) + ((FiveSanDiego[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiveLA[1] - Destination[1]) ** 2) + ((FiveLA[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiveSacramento[1] - Destination[1]) ** 2) + ((FiveSacramento[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiveBorder[1] - Destination[1]) ** 2) + ((FiveBorder[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiveGrantsPass[1] - Destination[1]) ** 2) + ((FiveGrantsPass[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FivePortland[1] - Destination[1]) ** 2) + ((FivePortland[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiveSeattle[1] - Destination[1]) ** 2) + ((FiveSeattle[0] - Destination[0]) ** 2)))

    ##Interstate 15
    IDList.append(sqrt(((FifteenSanDiego[1] - Destination[1]) ** 2) + ((FifteenSanDiego[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FifteenBarstow[1] - Destination[1]) ** 2) + ((FifteenBarstow[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FifteenVegas[1] - Destination[1]) ** 2) + ((FifteenVegas[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FifteenStGeorge[1] - Destination[1]) ** 2) + ((FifteenStGeorge[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FifteenSLC[1] - Destination[1]) ** 2) + ((FifteenSLC[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FifteenPocatello[1] - Destination[1]) ** 2) + ((FifteenPocatello[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FifteenBorder[1] - Destination[1]) ** 2) + ((FifteenBorder[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FifteenHelena[1] - Destination[1]) ** 2) + ((FifteenHelena[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FifteenCanada[1] - Destination[1]) ** 2) + ((FifteenCanada[0] - Destination[0]) ** 2)))

    ##Interstate 25
    IDList.append(sqrt(((TwentyFiveElPaso[1] - Destination[1]) ** 2) + ((TwentyFiveElPaso[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((TwentyFiveLasCruces[1] - Destination[1]) ** 2) + ((TwentyFiveLasCruces[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((TwentyFiveAlbuqurque[1] - Destination[1]) ** 2) + ((TwentyFiveAlbuqurque[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((TwentyFiveBorder[1] - Destination[1]) ** 2) + ((TwentyFiveBorder[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((TwentyFiveCheyenne[1] - Destination[1]) ** 2) + ((TwentyFiveCheyenne[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((TwentyFiveCasper[1] - Destination[1]) ** 2) + ((TwentyFiveCasper[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((TwentyFiveSheridan[1] - Destination[1]) ** 2) + ((TwentyFiveSheridan[0] - Destination[0]) ** 2)))

    ##Interstate 35
    IDList.append(sqrt(((ThirtyFiveLaredo[1] - Destination[1]) ** 2) + ((ThirtyFiveLaredo[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((ThirtyFiveSanAntonio[1] - Destination[1]) ** 2) + ((ThirtyFiveSanAntonio[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((ThirtyFiveDallas[1] - Destination[1]) ** 2) + ((ThirtyFiveDallas[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((ThirtyFiveOklahomaCity[1] - Destination[1]) ** 2) + ((ThirtyFiveOklahomaCity[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((ThirtyFiveWichita[1] - Destination[1]) ** 2) + ((ThirtyFiveWichita[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((ThirtyFiveKansasCity[1] - Destination[1]) ** 2) + ((ThirtyFiveKansasCity[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((ThirtyFiveDesMoines[1] - Destination[1]) ** 2) + ((ThirtyFiveDesMoines[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((ThirtyFiveAlbertLea[1] - Destination[1]) ** 2) + ((ThirtyFiveAlbertLea[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((ThirtyFiveMinneapolis[1] - Destination[1]) ** 2) + ((ThirtyFiveMinneapolis[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((ThirtyFiveDuluth[1] - Destination[1]) ** 2) + ((ThirtyFiveDuluth[0] - Destination[0]) ** 2)))

    ##Interstate 55
    IDList.append(
        sqrt(((FiftyFiveNewOrleans[1] - Destination[1]) ** 2) + ((FiftyFiveNewOrleans[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiftyFiveHammond[1] - Destination[1]) ** 2) + ((FiftyFiveHammond[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiftyFiveJackson[1] - Destination[1]) ** 2) + ((FiftyFiveJackson[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FiftyFiveBatesville[1] - Destination[1]) ** 2) + ((FiftyFiveBatesville[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiftyFiveMemphis[1] - Destination[1]) ** 2) + ((FiftyFiveMemphis[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FiftyFiveScottCity[1] - Destination[1]) ** 2) + ((FiftyFiveScottCity[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FiftyFiveBloomsdale[1] - Destination[1]) ** 2) + ((FiftyFiveBloomsdale[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiftyFiveStLouis[1] - Destination[1]) ** 2) + ((FiftyFiveStLouis[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiftyFiveMtOlive[1] - Destination[1]) ** 2) + ((FiftyFiveMtOlive[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FiftyFiveSpringfield[1] - Destination[1]) ** 2) + ((FiftyFiveSpringfield[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FiftyFiveBloomington[1] - Destination[1]) ** 2) + ((FiftyFiveBloomington[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiftyFiveDwight[1] - Destination[1]) ** 2) + ((FiftyFiveDwight[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FiftyFiveBolingbrook[1] - Destination[1]) ** 2) + ((FiftyFiveBolingbrook[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FiftyFiveChicago[1] - Destination[1]) ** 2) + ((FiftyFiveChicago[0] - Destination[0]) ** 2)))

    ##Interstate 65
    IDList.append(sqrt(((SixtyFiveMobile[1] - Destination[1]) ** 2) + ((SixtyFiveMobile[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveGreenville[1] - Destination[1]) ** 2) + ((SixtyFiveGreenville[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveMontgomery[1] - Destination[1]) ** 2) + ((SixtyFiveMontgomery[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SixtyFiveDecatur[1] - Destination[1]) ** 2) + ((SixtyFiveDecatur[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveFrankewing[1] - Destination[1]) ** 2) + ((SixtyFiveFrankewing[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveNashville[1] - Destination[1]) ** 2) + ((SixtyFiveNashville[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveBowlingGreen[1] - Destination[1]) ** 2) + ((SixtyFiveBowlingGreen[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveElizabethtown[1] - Destination[1]) ** 2) + ((SixtyFiveElizabethtown[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveLouisville[1] - Destination[1]) ** 2) + ((SixtyFiveLouisville[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveScottsburg[1] - Destination[1]) ** 2) + ((SixtyFiveScottsburg[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SixtyFiveColumbus[1] - Destination[1]) ** 2) + ((SixtyFiveColumbus[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveIndianapolis[1] - Destination[1]) ** 2) + ((SixtyFiveIndianapolis[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveLafayette[1] - Destination[1]) ** 2) + ((SixtyFiveLafayette[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SixtyFiveRemington[1] - Destination[1]) ** 2) + ((SixtyFiveRemington[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SixtyFiveGary[1] - Destination[1]) ** 2) + ((SixtyFiveGary[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((NinetyFourChicago[1] - Destination[1]) ** 2) + ((NinetyFourChicago[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((NinetyFourBorder[1] - Destination[1]) ** 2) + ((NinetyFourBorder[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FortyOneMtPleasant[1] - Destination[1]) ** 2) + ((FortyOneMtPleasant[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyOneMilwaukee[1] - Destination[1]) ** 2) + ((FortyOneMilwaukee[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FortyThreeSheboygan[1] - Destination[1]) ** 2) + ((FortyThreeSheboygan[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FortyThreeGreenBay[1] - Destination[1]) ** 2) + ((FortyThreeGreenBay[0] - Destination[0]) ** 2)))

    ##Interstate 75
    IDList.append(sqrt(((SeventyFiveMiami[1] - Destination[1]) ** 2) + ((SeventyFiveMiami[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveFortMyers[1] - Destination[1]) ** 2) + ((SeventyFiveFortMyers[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(
        ((SeventyFivePortCharlotte[1] - Destination[1]) ** 2) + ((SeventyFivePortCharlotte[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFiveTampa[1] - Destination[1]) ** 2) + ((SeventyFiveTampa[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFiveOcala[1] - Destination[1]) ** 2) + ((SeventyFiveOcala[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveGainesville[1] - Destination[1]) ** 2) + ((SeventyFiveGainesville[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveValdosta[1] - Destination[1]) ** 2) + ((SeventyFiveValdosta[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFiveTifton[1] - Destination[1]) ** 2) + ((SeventyFiveTifton[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFiveVienna[1] - Destination[1]) ** 2) + ((SeventyFiveVienna[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFivePerry[1] - Destination[1]) ** 2) + ((SeventyFivePerry[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFiveMacon[1] - Destination[1]) ** 2) + ((SeventyFiveMacon[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveAtlanta[1] - Destination[1]) ** 2) + ((SeventyFiveAtlanta[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveCalhoun[1] - Destination[1]) ** 2) + ((SeventyFiveCalhoun[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveChattanooga[1] - Destination[1]) ** 2) + ((SeventyFiveChattanooga[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveKnoxville[1] - Destination[1]) ** 2) + ((SeventyFiveKnoxville[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveLondon[1] - Destination[1]) ** 2) + ((FortyThreeGreenBay[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveLexington[1] - Destination[1]) ** 2) + ((SeventyFiveLexington[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveCincinnati[1] - Destination[1]) ** 2) + ((SeventyFiveCincinnati[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFiveDayton[1] - Destination[1]) ** 2) + ((SeventyFiveDayton[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveWapakoneta[1] - Destination[1]) ** 2) + ((SeventyFiveWapakoneta[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFiveBeaverdam[1] - Destination[1]) ** 2) + ((SeventyFiveBeaverdam[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFiveToledo[1] - Destination[1]) ** 2) + ((SeventyFiveToledo[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFiveMonroe[1] - Destination[1]) ** 2) + ((SeventyFiveMonroe[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((SeventyFivePontiac[1] - Destination[1]) ** 2) + ((SeventyFivePontiac[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((SeventyFiveFlint[1] - Destination[1]) ** 2) + ((SeventyFiveFlint[0] - Destination[0]) ** 2)))

    ##Interstate 95
    IDList.append(sqrt(((NinetyFiveMiami[1] - Destination[1]) ** 2) + ((NinetyFiveMiami[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(
        ((NinetyFiveWestPalmBeach[1] - Destination[1]) ** 2) + ((NinetyFiveWestPalmBeach[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveDaytonaBeach[1] - Destination[1]) ** 2) + ((NinetyFiveDaytonaBeach[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveStAugustine[1] - Destination[1]) ** 2) + ((NinetyFiveStAugustine[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveJacksonville[1] - Destination[1]) ** 2) + ((NinetyFiveJacksonville[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveSavannah[1] - Destination[1]) ** 2) + ((NinetyFiveSavannah[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveRosinville[1] - Destination[1]) ** 2) + ((NinetyFiveRosinville[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveFlorence[1] - Destination[1]) ** 2) + ((NinetyFiveFlorence[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveLumberton[1] - Destination[1]) ** 2) + ((NinetyFiveLumberton[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveFayetteville[1] - Destination[1]) ** 2) + ((NinetyFiveFayetteville[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveSmithfield[1] - Destination[1]) ** 2) + ((NinetyFiveSmithfield[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((NinetyFiveEmporia[1] - Destination[1]) ** 2) + ((NinetyFiveEmporia[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveRichmond[1] - Destination[1]) ** 2) + ((NinetyFiveRichmond[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(
        ((NinetyFiveFredericksburg[1] - Destination[1]) ** 2) + ((NinetyFiveFredericksburg[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveWashington[1] - Destination[1]) ** 2) + ((NinetyFiveWashington[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveWilmington[1] - Destination[1]) ** 2) + ((NinetyFiveWilmington[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFivePhiladelphia[1] - Destination[1]) ** 2) + ((NinetyFivePhiladelphia[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((NinetyFiveNewark[1] - Destination[1]) ** 2) + ((NinetyFiveNewark[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveStamford[1] - Destination[1]) ** 2) + ((NinetyFiveStamford[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveBridgeport[1] - Destination[1]) ** 2) + ((NinetyFiveBridgeport[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveNewHaven[1] - Destination[1]) ** 2) + ((NinetyFiveNewHaven[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFiveProvidence[1] - Destination[1]) ** 2) + ((NinetyFiveProvidence[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((NinetyFiveBoston[1] - Destination[1]) ** 2) + ((NinetyFiveBoston[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((NinetyFivePortsmouth[1] - Destination[1]) ** 2) + ((NinetyFivePortsmouth[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((NinetyFiveBangor[1] - Destination[1]) ** 2) + ((NinetyFiveBangor[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((NinetyFiveBorder[1] - Destination[1]) ** 2) + ((NinetyFiveBorder[0] - Destination[0]) ** 2)))

    ##Interstate 40
    IDList.append(sqrt(((FortyBarstow[1] - Destination[1]) ** 2) + ((FortyBarstow[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyKingman[1] - Destination[1]) ** 2) + ((FortyKingman[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyFlagstaff[1] - Destination[1]) ** 2) + ((FortyFlagstaff[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyGallup[1] - Destination[1]) ** 2) + ((FortyGallup[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyAlbuquerque[1] - Destination[1]) ** 2) + ((FortyAlbuquerque[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyAmarillo[1] - Destination[1]) ** 2) + ((FortyAmarillo[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyOklahomaCity[1] - Destination[1]) ** 2) + ((FortyOklahomaCity[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyLittleRock[1] - Destination[1]) ** 2) + ((FortyLittleRock[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyMemphis[1] - Destination[1]) ** 2) + ((FortyMemphis[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyNashville[1] - Destination[1]) ** 2) + ((FortyNashville[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyAsheville[1] - Destination[1]) ** 2) + ((FortyAsheville[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyHickory[1] - Destination[1]) ** 2) + ((FortyHickory[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyWinstonSalem[1] - Destination[1]) ** 2) + ((FortyWinstonSalem[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyGreensboro[1] - Destination[1]) ** 2) + ((FortyGreensboro[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyBurlington[1] - Destination[1]) ** 2) + ((FortyBurlington[0] - Destination[0]) ** 2)))
    IDList.append(
        sqrt(((FortyRaleighDurham[1] - Destination[1]) ** 2) + ((FortyRaleighDurham[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyBenson[1] - Destination[1]) ** 2) + ((FortyBenson[0] - Destination[0]) ** 2)))
    IDList.append(sqrt(((FortyWilmington[1] - Destination[1]) ** 2) + ((FortyWilmington[0] - Destination[0]) ** 2)))

    minValueHighwayDestination = min(IDList)
    indexValueHighwayDestination = IDList.index(
        minValueHighwayDestination)  ##https://pythonexamples.org/python-find-index-of-item-in-list/

    highwayD = []
    if indexValueHighwayDestination == 0:  ##five
        highwayD = FiveSanDiego.copy()
    elif indexValueHighwayDestination == 1:
        highwayD = FiveLA.copy()
    elif indexValueHighwayDestination == 2:
        highwayD = FiveSacramento.copy()
    elif indexValueHighwayDestination == 3:
        highwayD = FiveBorder.copy()
    elif indexValueHighwayDestination == 4:
        highwayD = FiveGrantsPass.copy()
    elif indexValueHighwayDestination == 5:
        highwayD = FivePortland.copy()
    elif indexValueHighwayDestination == 6:
        highwayD = FiveSeattle.copy()
    elif indexValueHighwayDestination == 7:  ##fifteen
        highwayD = FifteenSanDiego.copy()
    elif indexValueHighwayDestination == 8:
        highwayD = FifteenBarstow.copy()
    elif indexValueHighwayDestination == 9:
        highwayD = FifteenVegas.copy()
    elif indexValueHighwayDestination == 10:
        highwayD = FifteenStGeorge.copy()
    elif indexValueHighwayDestination == 11:
        highwayD = FifteenSLC.copy()
    elif indexValueHighwayDestination == 12:
        highwayD = FifteenPocatello.copy()
    elif indexValueHighwayDestination == 13:
        highwayD = FifteenBorder.copy()
    elif indexValueHighwayDestination == 14:
        highwayD = FifteenHelena.copy()
    elif indexValueHighwayDestination == 15:
        highwayD = FifteenCanada.copy()
    elif indexValueHighwayDestination == 16:  ##twenty five
        highwayD = TwentyFiveElPaso.copy()
    elif indexValueHighwayDestination == 17:
        highwayD = TwentyFiveLasCruces.copy()
    elif indexValueHighwayDestination == 18:
        highwayD = TwentyFiveAlbuqurque.copy()
    elif indexValueHighwayDestination == 19:
        highwayD = TwentyFiveCheyenne.copy()
    elif indexValueHighwayDestination == 20:
        highwayD = TwentyFiveCasper.copy()
    elif indexValueHighwayDestination == 21:
        highwayD = TwentyFiveSheridan.copy()
    elif indexValueHighwayDestination == 22:  ##thirty five
        highwayD = ThirtyFiveLaredo.copy()
    elif indexValueHighwayDestination == 23:
        highwayD = ThirtyFiveSanAntonio.copy()
    elif indexValueHighwayDestination == 24:
        highwayD = ThirtyFiveDallas.copy()
    elif indexValueHighwayDestination == 25:
        highwayD = ThirtyFiveOklahomaCity.copy()
    elif indexValueHighwayDestination == 26:
        highwayD = ThirtyFiveWichita.copy()
    elif indexValueHighwayDestination == 27:
        highwayD = ThirtyFiveKansasCity.copy()
    elif indexValueHighwayDestination == 28:
        highwayD = ThirtyFiveDesMoines.copy()
    elif indexValueHighwayDestination == 29:
        highwayD = ThirtyFiveAlbertLea.copy()
    elif indexValueHighwayDestination == 30:
        highwayD = ThirtyFiveMinneapolis.copy()
    elif indexValueHighwayDestination == 31:
        highwayD = ThirtyFiveDuluth.copy()
    elif indexValueHighwayDestination == 32:  ##fifty five
        highwayD = FiftyFiveNewOrleans.copy()
    elif indexValueHighwayDestination == 33:
        highwayD = FiftyFiveHammond.copy()
    elif indexValueHighwayDestination == 34:
        highwayD = FiftyFiveJackson.copy()
    elif indexValueHighwayDestination == 35:
        highwayD = FiftyFiveBatesville.copy()
    elif indexValueHighwayDestination == 36:
        highwayD = FiftyFiveMemphis.copy()
    elif indexValueHighwayDestination == 37:
        highwayD = FiftyFiveScottCity.copy()
    elif indexValueHighwayDestination == 38:
        highwayD = FiftyFiveBloomsdale.copy()
    elif indexValueHighwayDestination == 39:
        highwayD = FiftyFiveStLouis.copy()
    elif indexValueHighwayDestination == 40:
        highwayD = FiftyFiveMtOlive.copy()
    elif indexValueHighwayDestination == 41:
        highwayD = FiftyFiveSpringfield.copy()
    elif indexValueHighwayDestination == 42:
        highwayD = FiftyFiveBloomington.copy()
    elif indexValueHighwayDestination == 43:
        highwayD = FiftyFiveDwight.copy()
    elif indexValueHighwayDestination == 44:
        highwayD = FiftyFiveBolingbrook.copy()
    elif indexValueHighwayDestination == 45:
        highwayD = FiftyFiveChicago.copy()
    elif indexValueHighwayDestination == 46:  ##sixty five
        highwayD = SixtyFiveMobile.copy()
    elif indexValueHighwayDestination == 47:
        highwayD = SixtyFiveGreenville.copy()
    elif indexValueHighwayDestination == 48:
        highwayD = SixtyFiveMontgomery.copy()
    elif indexValueHighwayDestination == 49:
        highwayD = SixtyFiveDecatur.copy()
    elif indexValueHighwayDestination == 50:
        highwayD = SixtyFiveFrankewing.copy()
    elif indexValueHighwayDestination == 51:
        highwayD = SixtyFiveNashville.copy()
    elif indexValueHighwayDestination == 52:
        highwayD = SixtyFiveBowlingGreen.copy()
    elif indexValueHighwayDestination == 53:
        highwayD = SixtyFiveElizabethtown.copy()
    elif indexValueHighwayDestination == 54:
        highwayD = SixtyFiveLouisville.copy()
    elif indexValueHighwayDestination == 55:
        highwayD = SixtyFiveScottsburg.copy()
    elif indexValueHighwayDestination == 56:
        highwayD = SixtyFiveColumbus.copy()
    elif indexValueHighwayDestination == 57:
        highwayD = SixtyFiveIndianapolis.copy()
    elif indexValueHighwayDestination == 58:
        highwayD = SixtyFiveLafayette.copy()
    elif indexValueHighwayDestination == 59:
        highwayD = SixtyFiveRemington.copy()
    elif indexValueHighwayDestination == 60:
        highwayD = SixtyFiveGary.copy()
    elif indexValueHighwayDestination == 61:
        highwayD = NinetyFourChicago.copy()
    elif indexValueHighwayDestination == 62:
        highwayD = NinetyFourBorder.copy()
    elif indexValueHighwayDestination == 63:
        highwayD = FortyOneMtPleasant.copy()
    elif indexValueHighwayDestination == 64:
        highwayD = FortyOneMilwaukee.copy()
    elif indexValueHighwayDestination == 65:
        highwayD = FortyThreeSheboygan.copy()
    elif indexValueHighwayDestination == 66:
        highwayD = FortyThreeGreenBay.copy()
    elif indexValueHighwayDestination == 67:  ##seventy five
        highwayD = SeventyFiveMiami.copy()
    elif indexValueHighwayDestination == 68:
        highwayD = SeventyFiveFortMyers.copy()
    elif indexValueHighwayDestination == 69:
        highwayD = SeventyFivePortCharlotte.copy()
    elif indexValueHighwayDestination == 70:
        highwayD = SeventyFiveTampa.copy()
    elif indexValueHighwayDestination == 71:
        highwayD = SeventyFiveOcala.copy()
    elif indexValueHighwayDestination == 72:
        highwayD = SeventyFiveGainesville.copy()
    elif indexValueHighwayDestination == 73:
        highwayD = SeventyFiveValdosta.copy()
    elif indexValueHighwayDestination == 74:
        highwayD = SeventyFiveTifton.copy()
    elif indexValueHighwayDestination == 75:
        highwayD = SeventyFiveVienna.copy()
    elif indexValueHighwayDestination == 76:
        highwayD = SeventyFivePerry.copy()
    elif indexValueHighwayDestination == 77:
        highwaydD = SeventyFiveMacon.copy()
    elif indexValueHighwayDestination == 78:
        highwayD = SeventyFiveAtlanta.copy()
    elif indexValueHighwayDestination == 79:
        highwayD = SeventyFiveCalhoun.copy()
    elif indexValueHighwayDestination == 80:
        highwayD = SeventyFiveChattanooga.copy()
    elif indexValueHighwayDestination == 81:
        highwayD = SeventyFiveKnoxville.copy()
    elif indexValueHighwayDestination == 82:
        highwayD = SeventyFiveLondon.copy()
    elif indexValueHighwayDestination == 83:
        highwayD = SeventyFiveLexington.copy()
    elif indexValueHighwayDestination == 84:
        highwayD = SeventyFiveCincinnati.copy()
    elif indexValueHighwayDestination == 85:
        highwayD = SeventyFiveDayton.copy()
    elif indexValueHighwayDestination == 86:
        highwayD = SeventyFiveWapakoneta.copy()
    elif indexValueHighwayDestination == 87:
        highwayD = SeventyFiveBeaverdam.copy()
    elif indexValueHighwayDestination == 88:
        highwayD = SeventyFiveToledo.copy()
    elif indexValueHighwayDestination == 89:
        highwayD = SeventyFiveMonroe.copy()
    elif indexValueHighwayDestination == 90:
        highwayD = SeventyFivePontiac.copy()
    elif indexValueHighwayDestination == 91:
        highwayD = SeventyFiveFlint.copy()
    elif indexValueHighwayDestination == 92:  ##ninety five
        highwayD = NinetyFiveMiami.copy()
    elif indexValueHighwayDestination == 93:
        highwayD = NinetyFiveWestPalmBeach.copy()
    elif indexValueHighwayDestination == 94:
        highwayD = NinetyFiveDaytonaBeach.copy()
    elif indexValueHighwayDestination == 95:
        highwayD = NinetyFiveStAugustine.copy()
    elif indexValueHighwayDestination == 96:
        highwayD = NinetyFiveJacksonville.copy()
    elif indexValueHighwayDestination == 97:
        highwayD = NinetyFiveSavannah.copy()
    elif indexValueHighwayDestination == 98:
        highwayD = NinetyFiveRosinville.copy()
    elif indexValueHighwayDestination == 99:
        highwayD = NinetyFiveFlorence.copy()
    elif indexValueHighwayDestination == 100:
        highwayD = NinetyFiveFlorence.copy()
    elif indexValueHighwayDestination == 101:
        highwayD = NinetyFiveLumberton.copy()
    elif indexValueHighwayDestination == 102:
        highwayD = NinetyFiveFayetteville.copy()
    elif indexValueHighwayDestination == 103:
        highwayD = NinetyFiveSmithfield.copy()
    elif indexValueHighwayDestination == 104:
        highwayD = NinetyFiveEmporia.copy()
    elif indexValueHighwayDestination == 105:
        highwayD = NinetyFiveRichmond.copy()
    elif indexValueHighwayDestination == 106:
        highwayD = NinetyFiveFredericksburg.copy()
    elif indexValueHighwayDestination == 107:
        highwayD = NinetyFiveWashington.copy()
    elif indexValueHighwayDestination == 108:
        highwayD = NinetyFiveWilmington.copy()
    elif indexValueHighwayDestination == 109:
        highwayD = NinetyFivePhiladelphia.copy()
    elif indexValueHighwayDestination == 110:
        highwayD = NinetyFiveNewark.copy()
    elif indexValueHighwayDestination == 111:
        highwayD = NinetyFiveStamford.copy()
    elif indexValueHighwayDestination == 112:
        highwayD = NinetyFiveBridgeport.copy()
    elif indexValueHighwayDestination == 113:
        highwayD = NinetyFiveNewHaven.copy()
    elif indexValueHighwayDestination == 114:
        highwayD = NinetyFiveProvidence.copy()
    elif indexValueHighwayDestination == 115:
        highwayD = NinetyFiveBoston.copy()
    elif indexValueHighwayDestination == 116:
        highwayD = NinetyFivePortsmouth.copy()
    elif indexValueHighwayDestination == 117:
        highwayD = NinetyFiveBangor.copy()
    elif indexValueHighwayDestination == 118:
        highwayD = NinetyFiveBorder.copy()
    elif indexValueHighwayDestination == 119:  ##forty
        highwayD = FortyBarstow.copy()
    elif indexValueHighwayDestination == 120:
        highwayD = FortyKingman.copy()
    elif indexValueHighwayDestination == 121:
        highwayD = FortyFlagstaff.copy()
    elif indexValueHighwayDestination == 122:
        highwayD = FortyGallup.copy()
    elif indexValueHighwayDestination == 123:
        highwayD = FortyAlbuquerque.copy()
    elif indexValueHighwayDestination == 124:
        highwayD = FortyAmarillo.copy()
    elif indexValueHighwayDestination == 125:
        highwayD = FortyOklahomaCity.copy()
    elif indexValueHighwayDestination == 126:
        highwayD = FortyLittleRock.copy()
    elif indexValueHighwayDestination == 127:
        highwayD = FortyMemphis.copy()
    elif indexValueHighwayDestination == 128:
        highwayD = FortyNashville.copy()
    elif indexValueHighwayDestination == 129:
        highwayD = FortyAsheville.copy()
    elif indexValueHighwayDestination == 130:
        highwayD = FortyHickory.copy()
    elif indexValueHighwayDestination == 131:
        highwayD = FortyWinstonSalem.copy()
    elif indexValueHighwayDestination == 132:
        highwayD = FortyGreensboro.copy()
    elif indexValueHighwayDestination == 133:
        highwayD = FortyBurlington.copy()
    elif indexValueHighwayDestination == 134:
        highwayD = FortyRaleighDurham.copy()
    elif indexValueHighwayDestination == 135:
        highwayD = FortyBenson.copy()
    elif indexValueHighwayDestination == 136:
        highwayD = FortyWilmington.copy()

    return highwayD




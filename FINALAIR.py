def distanceOriCalc(x1, y1):
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


##Distance from destination to closest airport



def distanceDestCalc(x2, y2):
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
def planeDistance(oriAirport, DestAirport):
    x1a = oriAirport[0]
    y1a = oriAirport[1]
    x2a = DestAirport[0]
    y2a = DestAirport[1]
    return (sqrt(((y2a - y1a) ** 2) + ((x2a - x1a) ** 2)))




def pixelsToCoordinates(x, y):
  longScale = 262.384
  latScale = 196.63
  longRight = -61.874370
  latBottom = 24.415332
  xDif = 800 - x
  yDif = 400 - y
  Long = ((longRight * 3600) - (xDif * longScale)) / 3600
  Lat = ((latBottom * 3600) + (yDif * latScale)) / 3600
  return Long, Lat
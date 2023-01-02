from math import sqrt

t = int(input())

powers = {
    "fire": {
        "dmg": 200,
        1: 20,
        2: 30,
        3: 50
    },
    "water" : {
        "dmg": 300,
        1: 10,
        2: 25,
        3: 40
    },
    "earth" : {
        "dmg": 400,
        1: 25,
        2: 55,
        3: 70
    },
    "air" : {
        "dmg": 100,
        1: 18,
        2: 38,
        3: 60
    }
}

for i in range(t):
    w, h, x0, y0 = input().split()
    w = int(w)
    h = int(h)
    x0 = int(x0)
    y0 = int(y0)

    power, n, cx, cy = input().split()
    n = int(n)
    cx = int(cx)
    cy = int(cy)
    
    range = powers[power][n]
    dmg = powers[power]["dmg"]
    distanceLeftBottom = sqrt(pow(abs(x0 - cx),2) + pow(abs(y0 - cy),2))
    distanceLeftUpper = sqrt(pow(abs(x0 - cx),2) + pow(abs(y0 + h - cy),2))
    distanceRightUpper = sqrt(pow(abs(x0 + w - cx),2) + pow(abs(y0 + h - cy),2))
    distanceRightBottom = sqrt(pow(abs(x0 + w - cx),2) + pow(abs(y0 - cy),2))
    
    
    distanceLeftBottomToRightBottom = sqrt(pow(abs(y0 - cy),2)) if cx > x0 and cx < x0 + w else None
    distanceLeftUpperToRightUpper = sqrt(pow(abs(y0 + h - cy),2)) if cx > x0 and cx < x0 + w else None
    distanceLeftUpperToLeftBottom = sqrt(pow(abs(x0 - cx),2)) if cy > y0 and cy < y0 + h else None
    distanceRightUpperToRightBottom = sqrt(pow(abs(x0 + w - cx),2)) if cy > y0 and cy < y0 + h else None
     
    distancesList = [distanceLeftBottom, distanceLeftUpper, distanceRightUpper, distanceRightBottom, distanceLeftBottomToRightBottom, distanceLeftUpperToRightUpper, distanceLeftUpperToLeftBottom, distanceRightUpperToRightBottom]
    distancesListWithoutBolleans = [item for item in distancesList if item != None]
    distancesListWithoutBolleans.sort()
    smallerDistance = distancesListWithoutBolleans[0]
    if smallerDistance <= range or (cx > x0 and cx < x0 + w and cy > y0 and cy < y0 + h):
        print(dmg)
    else:
        print(0)

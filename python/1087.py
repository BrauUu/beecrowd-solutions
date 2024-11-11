qs = {
    1 : {
        "x" : +1,
        "y" : -1
    },
    2 : {
        "x" : -1,
        "y" : -1
    },
    3 : {
        "x" : -1,
        "y" : +1
    },
    4 : {
        "x" : +1,
        "y" : +1
    }
}

q = 0

while True:
    x1, y1, x2, y2 = input().split()
    x1 = int(x1)
    y1 = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    
    isTwoMoves = False
    
    if x1 == x2 == y1 == y2 == 0:
        break

    actualPos = {"x" : x1, "y" : y1}
    objPos = {"x" : x2, "y" : y2}

    if objPos["x"] == actualPos["x"] and objPos["y"] == actualPos["y"]:
        print(0)
    elif objPos["x"] == actualPos["x"] or objPos["y"] == actualPos["y"]:
        print(1)
    else:
        if objPos["x"] > actualPos["x"]:
            if objPos["y"] > actualPos["y"]:
                q = 4
            elif objPos["y"] < actualPos["y"]:
                q = 1
        elif objPos["x"] < actualPos["x"]:
            if objPos["y"] > actualPos["y"]:
                q = 3
            elif objPos["y"] < actualPos["y"]:
                q = 2
                
        while objPos != actualPos:
            if actualPos["x"] >= 9 or actualPos["x"] <= 0 or actualPos["y"] >= 9 and actualPos["y"] <= 0:
                print(2)
                isTwoMoves = True
                break
            actualPos["x"] += qs[q]["x"]
            actualPos["y"] += qs[q]["y"]
        if isTwoMoves == False:
            print(1)
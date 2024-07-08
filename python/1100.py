COORDINATES = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
}

def numberOfMovesToAChessKnightToGoFromOneCoordinateToAnother(board: list, startCoordinate: list, endCoordinate: list):
    availableCoordinates = [startCoordinate]
    tempAvailableCoordinates = []
    movesCount = 0
    while len(availableCoordinates):
        coordinate = availableCoordinates.pop(0)
        board[coordinate[0]][coordinate[1]] = 0
        moves = getMovements(board, coordinate)
        for move in moves:
            if move == endCoordinate:
                return movesCount + 1
            if availableCoordinates.count(move) == 0 and tempAvailableCoordinates.count(move) == 0:
                tempAvailableCoordinates.append(move)
        if len(availableCoordinates) == 0:
            movesCount += 1
            availableCoordinates += tempAvailableCoordinates

def getMovements(board: list, coordinate: list):
    y = coordinate[0]
    x = coordinate[1]
    boardLastIndex = len(board) - 1
    movements = []
    if x - 2 >= 0 and y - 1 >= 0:
        isANewMovement = board[y-1][x-2]
        if isANewMovement == 1:
            movements.append([y-1, x-2])
    if x - 1 >= 0 and y - 2 >= 0:
        isANewMovement = board[y-2][x-1]
        if isANewMovement == 1:
            movements.append([y-2, x-1])
    if x - 1 >= 0 and y + 2 <= boardLastIndex:
        isANewMovement = board[y+2][x-1]
        if isANewMovement == 1:
            movements.append([y+2, x-1])
    if x - 2 >= 0 and y + 1 <= boardLastIndex:
        isANewMovement = board[y+1][x-2]
        if isANewMovement == 1:
            movements.append([y+1, x-2])
    if x + 2 <= boardLastIndex and y - 1 >= 0:
        isANewMovement = board[y-1][x+2]
        if isANewMovement == 1:
            movements.append([y-1, x+2])
    if x + 1 <= boardLastIndex and y - 2 >= 0:
        isANewMovement = board[y-2][x+1]
        if isANewMovement == 1:
            movements.append([y-2, x+1])
    if x + 2 <= boardLastIndex and y + 1 <= boardLastIndex:
        isANewMovement = board[y+1][x+2]
        if isANewMovement == 1:
            movements.append([y+1, x+2])
    if x + 1 <= boardLastIndex and y + 2 <= boardLastIndex:
        isANewMovement = board[y+2][x+1]
        if isANewMovement == 1:
            movements.append([y+2, x+1])
    return movements

while True:
    try:
        board = [[1 for _ in range(8)] for _ in range(8)]
        x, y = input().split()
        x1 = COORDINATES[x[0]]
        x2 = int(x[1]) - 1
        y1 = COORDINATES[y[0]]
        y2 = int(y[1]) - 1
        startCoordinate = [x1, x2]
        endCoordinate = [y1, y2]
        movesCount = numberOfMovesToAChessKnightToGoFromOneCoordinateToAnother(board, startCoordinate, endCoordinate)
        print(f'To get from {x} to {y} takes {movesCount} knight moves.')
    except:
        break
def canCopsGetRobbers(maze: list, start: list, end: list):
    availableCells = []
    if maze[start[0]][start[1]] == 0:
        availableCells.append(start)
    exploredCells = []
    while len(availableCells):
        cell = availableCells.pop(0)
        if cell == end:
            return True
        exploredCells.append(cell)
        neighborhood = getNeighborhood(maze, cell)
        for neighbor in neighborhood:
            if exploredCells.count(neighbor) == 0 and availableCells.count(neighbor) == 0:
                availableCells.append(neighbor)
    return False

def getNeighborhood(maze, cell):
    y = cell[0]
    x = cell[1]
    neighborhood = []
    if y != 0:
        v = maze[y-1][x]
        if v == 0:
            neighborhood.append([y-1, x])
    if y < len(maze) - 1:
        v = maze[y+1][x]
        if v == 0:
            neighborhood.append([y+1, x])
    if x != 0:
        v = maze[y][x-1]
        if v == 0:
         neighborhood.append([y, x-1])
    if x < len(maze[0]) - 1:
        v = maze[y][x+1]
        if v == 0:
            neighborhood.append([y, x+1])
    return neighborhood

t = int(input())

start = [0,0]
end = [4,4]

for _ in range(t):

    maze = []
    i = 1
    while i <= 5:
        line = list(map(int, input().split()))
        if len(line) != 0:
            maze.append(line)
            i += 1
    boolean = canCopsGetRobbers(maze, start, end)
    print('COPS' if boolean else 'ROBBERS')
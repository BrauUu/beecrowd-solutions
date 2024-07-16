def move(case) :
    match case:
        case '>':
            ap['direction'] = '>'
            if ap['x'] == x - 1:
                return False
            ap['x'] += 1
        case '<':
            ap['direction'] = '<'
            if ap['x'] == 0:
                return False
            ap['x'] -= 1
        case 'v':
            ap['direction'] = 'v'
            if ap['y'] == y - 1:
                return False
            ap['y'] += 1
        case '^':
            ap['direction'] = '^'
            if ap['y'] == 0:
                return False
            ap['y'] -= 1
        case '.':
            move(ap['direction'])
    return True

x = int(input())
y = int(input())
m = []
for _ in range(y):
    m.append(input())

ap = {
    'x': 0,
    'y': 0,
    'direction' : '',
}
traveledPath = []
treasureFound = False
while True:
    case = m[ap['y']][ap['x']]
    if traveledPath.count((ap['y'], ap['x'])) != 0:
        break
    traveledPath.append((ap['y'], ap['x']))
    if move(case) == False:
        break
    if case == '*':
        treasureFound = True
        break
print('*' if treasureFound else '!')
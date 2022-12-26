pos, dest = input().split()

posX = int(ord(pos[0]) - 96)
posY = int(pos[1])

destX = int(ord(dest[0]) - 96)
destY = int(dest[1])

if posX + 1 == destX and posY + 2 == destY:
    print('VALIDO')
elif posX - 1 == destX and posY + 2 == destY:
    print('VALIDO')
elif posX + 2 == destX and posY + 1 == destY:
    print('VALIDO')
elif posX - 2 == destX and posY + 1 == destY:
    print('VALIDO')
elif posX + 2 == destX and posY - 1 == destY:
    print('VALIDO')
elif posX - 2 == destX and posY - 1 == destY:
    print('VALIDO')
elif posX + 1 == destX and posY - 2 == destY:
    print('VALIDO')
elif posX - 1 == destX and posY - 2 == destY:
    print('VALIDO')
else:
    print('INVALIDO')

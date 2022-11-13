side01, side02, side03 = input().split()

side01 = int(side01)
side02 = int(side02)
side03 = int(side03)

sides = [side01, side02, side03]

sides.sort()

if sides[0] + sides[1] > sides[2] and sides[1] - sides[0] < sides[2]:
    if sides[0] == sides[1] and sides[1] == sides[2]:
        print('Valido-Equilatero')
    elif sides[0] == sides[1] or sides[0] == sides[2] or sides[2] == sides[1]:
        print('Valido-Isoceles')
    elif sides[0] != sides[1] and sides[0] != sides[2] and sides[2] != sides[1]:
        print('Valido-Escaleno')

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print('Retangulo: S')
    else:
        print('Retangulo: N')

else:
    print('Invalido')

x = int(input())

hexa = hex(x)
slicer = slice(2, len(hex(x)))

print(f'{hexa[slicer].upper()}')

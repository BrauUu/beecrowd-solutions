peopleThere = 0
carsThere = 0

while True:
     
    entries = input()
    
    if entries.find('ABEND') != -1:
        break
    
    mov, qty = entries.split()
    
    qty = int(qty)
    
    if mov == 'SALIDA':
        peopleThere += qty
        carsThere += 1
    if mov == 'VUELTA':
        peopleThere -= qty
        carsThere -= 1
        
print(peopleThere)
print(carsThere)
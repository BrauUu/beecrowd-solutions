obj = {
    0: 6,
    1 : 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

n = int(input())

for i in range(n):
    x = input()
    leds = 0    
    for i in range(len(x)):
        leds += obj[int(x[i])]
        
    print(f'{leds} leds')
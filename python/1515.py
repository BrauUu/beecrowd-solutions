while True:
    n = int(input())
    if n == 0:
        break
    smallest = 0
    planet = ''
    for i in range(n):
        name, yearDelivery, yearsToDeliver = input().split()
        y = int(yearDelivery) - int(yearsToDeliver)
        if i == 0:
            smallest = y
            planet = name
        elif y < smallest:
            smallest = y
            planet = name
    print(planet)
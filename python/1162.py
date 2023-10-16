from sys import stdout, stdin

def bubble_sort(lista, n):
    countB = 0
    for i in range(n):
        flag = False
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                countB += 1
                flag = True
                lista[j], lista[j+1] = lista[j+1], lista[j]
        if flag == False:
            break
    return countB         
        
n = int(stdin.readline())

for i in range(n):
    x = int(stdin.readline())
    cars = list(map(int, stdin.readline().split()))
    countB = bubble_sort(cars, x)
    stdout.write(f'Optimal train swapping takes {countB} swaps.\n')
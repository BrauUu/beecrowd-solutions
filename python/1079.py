n = int(input())

for i in range(n):
    numbers = input().split()
    n1 = float(numbers[0])
    n2 = float(numbers[1])
    n3 = float(numbers[2])
    
    avg = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
    print(f'{avg:.1f}')
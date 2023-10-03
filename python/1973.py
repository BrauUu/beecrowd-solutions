from sys import stdout, stdin

def main():

    n = int(stdin.readline())

    arr = list(map(int, stdin.readline().split()))
    sum = 0

    for i in range(n):
        sum += arr[i]

    actualStar = 0
    starCount = 1
    sheepStolenCount = 0

    while True:
        if actualStar < 0 or actualStar >= n or arr[actualStar] == 0:
            break

        if starCount < actualStar + 1:
            starCount += 1

        if arr[actualStar] % 2 == 0:
            arr[actualStar] -= 1
            actualStar -= 1
        elif arr[actualStar] % 2 == 1:
            arr[actualStar] -= 1
            actualStar += 1
            
        sheepStolenCount += 1

    stdout.write(str(starCount) + ' ' + str(sum - sheepStolenCount) + '\n')

if __name__ == "__main__":
    main()
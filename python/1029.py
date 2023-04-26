def fibonacci(n):
    callsCount[0] += 1
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())

for i in range(n):
    callsCount = [-1]
    x = int(input())
    response = fibonacci(x)
    print(f'fib({x}) = {callsCount[0]} calls = {response}')
    
# Fala que dá 'Time limit' no próximo
# Alternative

fibArr = [
    {"value": 0, "count": 0},
    {"value": 1, "count": 0},
    {"value": 1, "count": 2},
    {"value": 2, "count": 4},
    {"value": 3, "count": 8},
    {"value": 5, "count": 14},
    {"value": 8, "count": 24},
    {"value": 13, "count": 40},
    {"value": 21, "count": 66},
    {"value": 34, "count": 108},
    {"value": 55, "count": 176},
    {"value": 89, "count": 286},
    {"value": 144, "count": 464},
    {"value": 233, "count": 752},
    {"value": 377, "count": 1218},
    {"value": 610, "count": 1972},
    {"value": 987, "count": 3192},
    {"value": 1597, "count": 5166},
    {"value": 2584, "count": 8360},
    {"value": 4181, "count": 13528},
    {"value": 6765, "count": 21890},
    {"value": 10946, "count": 35420},
    {"value": 17711, "count": 57312},
    {"value": 28657, "count": 92734},
    {"value": 46368, "count": 150048},
    {"value": 75025, "count": 242784},
    {"value": 121393, "count": 392834},
    {"value": 196418, "count": 635620},
    {"value": 317811, "count": 1028456},
    {"value": 514229, "count": 1664078},
    {"value": 832040, "count": 2692536},
    {"value": 1346269, "count": 4356616},
    {"value": 2178309, "count": 7049154},
    {"value": 3524578, "count": 11405772},
    {"value": 5702887, "count": 18454928},
    {"value": 9227465, "count": 29860702},
    {"value": 14930352, "count": 48315632},
    {"value": 24157817, "count": 78176336},
    {"value": 39088169, "count": 126491970},
    {"value": 63245986, "count": 204668308},
]

n = int(input())

for i in range(n):
    x = int(input())
    print(f"fib({x}) = {fibArr[x]['count']} calls = {fibArr[x]['value']}")

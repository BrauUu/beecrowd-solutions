from math import sqrt

n = int(input())

print(f'{(((pow(((1 + sqrt(5))/2), n)) - (pow(((1 - sqrt(5))/2), n)))/ sqrt(5)):.1f}')
# Limite de memória
# def degrees(n):
#     l = [0] * (n + 1)
#     l[0] = 1
#     for i in range(1, n + 1):
#         l[i] = l[i - 1]
#         if i >= 2:
#             l[i] += l[i - 2]
#         if i >=3:
#             l[i] += l[i - 3]
#     return l[n]

def degrees(n):
    l = [0] * 4
    l[0] = 1
    for i in range(1, n + 1):
        g = i % 4
        l[g] = l[g - 1]
        if i >= 2:
            l[g] += l[g - 2]
        if i >=3:
            l[g] += l[g - 3]
    return l[n % 4]

n = int(input())
print(degrees(n) % (10 ** 9 + 7))
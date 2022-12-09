n = int(input())

a, b = input().split()
a = int(a)
b = int(b)

if a + b > n:
    print("Deixa para amanha!")
else:
    print("Farei hoje!")
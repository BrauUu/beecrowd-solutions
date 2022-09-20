n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 < n2 and n2 < n3:
    print(n1)
    print(n2)
    print(n3)
elif n2 < n1 and n1 < n3:
    print(n2)
    print(n1)
    print(n3)
elif n2 < n3 and n3 < n1:
    print(n2)
    print(n3)
    print(n1)
elif n1 < n3 and n3 < n2:
    print(n1)
    print(n3)
    print(n2)
elif n3 < n1 and n1 < n2:
    print(n3)
    print(n1)
    print(n2)
elif n3 < n2 and n2 < n1:
    print(n3)
    print(n2)
    print(n1)
    
print()
print(n1)
print(n2)
print(n3)
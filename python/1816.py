import string
i = 1
while True:
    n = int(input())
    if n == 0:
        break
    abc = list(string.ascii_uppercase)
    crypt = list(map(int, input().split()))
    word = ''
    for char in crypt:
        word += abc[char-1]
        abc.insert(0, abc[char-1])
        abc.pop(char)
    print(f'Instancia {i}\n{word}\n')
    i += 1
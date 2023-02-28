def decrypt(encripted, cipher):
    res = ''
    for char in encripted:
        code = ord(char) - cipher
        if code < 65:
            res += chr(code + 26)
        else:
            res += chr(code)
    return res

n = int(input())

for i in range(n):
    encripted = input()
    cipher = int(input())
    
    print(decrypt(encripted, cipher))
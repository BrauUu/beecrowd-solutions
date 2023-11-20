alphabet = {
    '=.===': "a",  # .-
    '===.=.=.=': 'b',  # -...
    '===.=.===.=': 'c',  # -.-.
    '===.=.=': 'd',  # -..
    '=': 'e',  # .
    '=.=.===.=': 'f',  # ..-.
    '===.===.=': 'g',  # --.
    '=.=.=.=': 'h',  # ....
    '=.=': 'i',  # ..
    '=.===.===.===': 'j',  # .---
    '===.=.===': 'k',  # -.-
    '=.===.=.=': 'l',  # .-..
    '===.===': 'm',  # --
    '===.=': 'n',  # -.
    '===.===.===': 'o',  # ---
    '=.===.===.=': 'p',  # .--.
    '===.===.=.===': 'q',  # --.-
    '=.===.=': 'r',  # .-.
    '=.=.=': 's',  # ...
    '===': 't',  # -
    '=.=.===': 'u',  # ..-
    '=.=.=.===': 'v',  # ...-
    '=.===.===': 'w',  # .--
    '===.=.=.===': 'x',  # -..-
    '===.=.===.===': 'y',  # -.--
    '===.===.=.=': 'z'  # --..
}

n = int(input())

for i in range(n):
    code = input()
    x = 0
    res = ''
    while True:
        z = code.find(".......", x)
        if z == -1 or code.find("...=", x, z) != -1:
            y = code.find("...", x)
            if y == -1:
                letter = code[x:]
                res += alphabet[letter]
                break
            letter = code[x:y]
            res += alphabet[letter]
            x = y+3
        else:
            letter = code[x:z]
            res += alphabet[letter]
            res += ' '
            x = z+7
            
    print(res)
        
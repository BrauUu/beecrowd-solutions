import re

while True:
    try:
        x = input()

        res = re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,32}$", x)
        if res != None:
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except:
        break

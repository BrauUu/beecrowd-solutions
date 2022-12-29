def lex(a, b, i=0):
    try:
        if ord(a[i]) == ord(b[i]):
            return lex(a, b, i + 1)
        else:
            if ord(a[i]) < ord(b[i]):
                return f"{a}\n{b}"
            else:
                return f"{b}\n{a}"
    except:
        return f"{a}\n{b}" if len(a) < len(b) else f"{b}\n{a}"


a = input()
b = input()

print(lex(a, b))

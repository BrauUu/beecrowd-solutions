from math import ceil

while True:
    try:
        n, l, c = map(int, input().split())
        text = input()

        lCount = 0

        i = c - 1
        while True:
            if i >= len(text) - 1:
                lCount += 1
                break
            elif text[i] == ' ':
                lCount += 1
            elif text[i + 1] == ' ':
                lCount += 1
                i += 1
            else:
                lastBlankSpaceIndex = text[:i].rfind(' ')
                i = lastBlankSpaceIndex
                lCount += 1
            i += c    
            
        print(str(ceil(lCount / l)))
    except:
        break

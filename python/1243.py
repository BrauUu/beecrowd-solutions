import re 
while True:
    try:
        words = input().split()
        s = 0
        c = 0
        avg = 0
        for word in words:
            countNum = len(re.findall('[0-9]', word))
            countPeriods = len(re.findall('\.', word))
            if countNum > 0 or countPeriods > 1:
                continue
            if countPeriods == 1:
                if word.index('.') < len(word) - 1:
                    continue
                s -= 1
            s += len(word)
            c += 1
        if c > 0:
            avg = s // c
        if avg <= 3:
            p = 250
        elif avg > 3 and avg <= 5:
            p = 500
        else:
            p = 1000
        print(p)
    except:
        break
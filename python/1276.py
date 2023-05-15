while True:
    try:
        x = input()

        initialCharCode = 97
        actualCharCode = initialCharCode
        res = ''
        actualCharCount = 0

        j = 0

        while True:
            actualChar = chr(actualCharCode)
            actualCharCount += x.count(actualChar)
            if x.count(actualChar) > 0:
                if j > 0:
                    res += f', {actualChar}:'
                else:
                    res += f'{actualChar}:'
                actualCharCode += 1
                actualChar = chr(actualCharCode)
                while x.count(actualChar) > 0:
                    actualCharCount += x.count(actualChar)
                    actualCharCode += 1
                    actualChar = chr(actualCharCode)
                res += f'{chr(actualCharCode - 1)}'
                j += 1
            else:
                actualCharCode += 1
                
            if actualCharCount + x.count(' ') == len(x):
                break
            
        print(res)
    except:
        break  
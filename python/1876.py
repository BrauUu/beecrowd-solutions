def middleCountFunc(string):
    bgst = 0
    seq = 0
    for char in string:
        if char == 'o':
            seq += 1
        elif char == 'x':
            if seq > bgst:
                bgst = seq
            seq = 0
    return bgst

while True:
    try:
        x = input()

        beginInd = x.find('x') if x.find('x') != -1 else 0
        endInd = x.rfind('x') if x.rfind('x') != -1 else 0

        beginCount = x[:beginInd+1].count('o')
        endCount = x[endInd:].count('o')
        middleCount = middleCountFunc(x[beginInd:endInd+1]) // 2
        
        print(max(beginCount, endCount, middleCount))

    except:
        break
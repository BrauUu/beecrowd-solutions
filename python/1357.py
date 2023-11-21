b = {
    '1' : ["*.", "..", ".."],
    '2' : ["*.", "*.", ".."],
    '3' : ["**", "..", ".."],
    '4' : ["**", ".*", ".."],
    '5' : ["*.", ".*", ".."],
    '6' : ["**", "*.", ".."],
    '7' : ["**", "**", ".."],
    '8' : ["*.", "**", ".."],
    '9' : [".*", "*.", ".."],
    '0' : [".*", "**", ".."],
}

nx = {
    "*....." : "1",
    "*.*..." : "2",
    "**...." : "3",
    "**.*.." : "4",
    "*..*.." : "5",
    "***..." : "6",
    "****.." : "7",
    "*.**.." : "8",
    ".**..." : "9",
    ".***.." : "0"
}

def numToBraille(num):
    res = ['', '', '']
    for char in num:
        res[0] += b[char][0] + ' '
        res[1] += b[char][1] + ' '
        res[2] += b[char][2] + ' '
    res[0] = res[0].rstrip()
    res[1] = res[1].rstrip()
    res[2] = res[2].rstrip()
    return res

def brailleToNum(s):
    res = ''
    for i in range(0, len(s[0]) - 1, 3):
        temp = ''
        temp += s[0][i: i + 2]
        temp += s[1][i: i + 2]
        temp += s[2][i: i + 2]
        res += nx[temp]
    return res

while True:
    n = int(input())
    
    if n == 0:
        break
    
    iType = input()
    
    match iType:
        case 'S':
            x = input()
            print(*numToBraille(x), sep="\n")
        case 'B':
            x = []
            x.append(input())
            x.append(input())
            x.append(input())
            print(brailleToNum(x))         
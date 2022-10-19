x = int(input())

def returnStringNTimes(string, times):
    ret = ''
    for i in range(times):
        ret += string
    return ret

word = ''

# Casa das centenas

countD = int(x / 500)
word += returnStringNTimes('D', countD)
x -= countD * 500

countC = int(x / 100)
ret = returnStringNTimes('C', countC)
# Se o retorno da função = 400
word += 'CD' if ret == 'CCCC' else ret
x -= countC * 100

# Se o valor das centenas = 900

if word == 'DCD':
    word = 'CM'
    
# Casa das dezenas
    
countL = int(x / 50)
word += returnStringNTimes('L', countL)
x -= countL * 50

countX = int(x / 10)
ret = returnStringNTimes('X', countX)
# Se o retorno da função = 40
word += 'XL' if ret == 'XXXX' else ret
x -= countX * 10

# Se valor das dezenas = 90
if word.find('LXL') >= 0:
    word = word[:word.find('LXL')]
    word += 'XC'
    
# Casa das unidades
    
countV = int(x / 5)
word += returnStringNTimes('V', countV)
x -= countV * 5

countI = int(x / 1)
ret = returnStringNTimes('I', countI)
# Se o retorno da função = 4
word += 'IV' if ret == 'IIII' else ret
x -= countI * 1

# Se valor das unidades = 9
if word.find('VIV') >= 0:
    word = word[:word.find('VIV')]
    word += 'IX'
            
print(word) 
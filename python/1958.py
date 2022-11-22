def returnMovementsNumber(value):
    if float(value) > 0:
        if value[0] == '0':
            for i in range(len(value)):
                if value[i].isalnum():
                    if int(value[i]) > 0:
                        return '-' + str(i - 1) if i - 1 >= 10 else '-0' + str(i - 1)  
        try :
            dotIndex = value.index('.')
            if dotIndex == 1:
                return '+00'
            else:
                return '+' + str(dotIndex - 1) if dotIndex - 1 >= 10 else '+0' + str(dotIndex - 1)
            
        except:
            return '+' + str(len(value) - 1) if len(value) - 1 >= 10 else '+0' + str(len(value) - 1)
    else:
        if value[1] == '0':
            for i in range(len(value)):
                if value[i].isalnum():
                    if int(value[i]) > 0:
                        return '-' + str(i - 2) if i - 2 >= 10 else '-0' + str(i - 2)  
        try :
            dotIndex = value.index('.')
            if dotIndex == 2:
                return '+00'
            else:
                return '+' + str(dotIndex - 2) if dotIndex - 2 >= 10 else '+0' + str(dotIndex - 2)
            
        except:
            return '+' + str(len(value) - 2) if len(value) - 2 >= 10 else '+0' + str(len(value) - 2)


value = input()
result = ''
signal = ''

if value[0] == '-':
    signal = '-'
    result += signal
else:
    signal = '+'
    result += signal
    
for i in range(len(value)):
    if value[i].isalnum():
        if int(value[i]) > 0:
            result += value[i] + '.'
            floatValue = value[i+1:]
            
            count = 0
            
            for j in range(len(floatValue)):
                char = floatValue[j]
                if char.isalnum():
                    
                    if count == 3:
                        try:
                            if int(floatValue[j+1]) >= 5:
                                count += 1
                                result += str(int(char) + 1)
                                break
                            else:
                                count += 1
                                result += char
                                break
                        except:
                            count = count
                    
                    result += char
                    count += 1
                    
            if count < 4:
                string = '0000'
                result += string[:4 - count]
            result += 'E' + returnMovementsNumber(value)
            break
  
if float(value) == 0:
    print(signal + '0.0000E+00')
else:      
    print(result)
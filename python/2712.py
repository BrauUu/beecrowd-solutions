import re

n = int(input())

for i in range(n):
    sign = input()
    if re.search('^[A-Z]{3}-[0-9]{4}$', sign) == None:
        print('FAILURE')
        continue
    lastChar = sign[len(sign) - 1] 
    
    if lastChar == '1' or lastChar == '2':
        print('MONDAY')
    if lastChar == '3' or lastChar == '4':
        print('TUESDAY')
    if lastChar == '5' or lastChar == '6':
        print('WEDNESDAY')
    if lastChar == '7' or lastChar == '8':
        print('THURSDAY')
    if lastChar == '9' or lastChar == '0':
        print('FRIDAY')
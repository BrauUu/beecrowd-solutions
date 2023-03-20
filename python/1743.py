x = input().replace(' ', '')
y = input().replace(' ', '')

flag = False

for i in range(5):
    if x[i] == y[i]:
        flag = True
        break
    
if flag == True:
    print('N')
else:
    print('Y')
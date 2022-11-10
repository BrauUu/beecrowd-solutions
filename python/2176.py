x = input()

count = 0

for i in x:
    if i == '1':
        count += 1
        
if count % 2 == 1:
    x = x + '1'
else:
    x = x + '0'
    
print(x)
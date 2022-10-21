n = int(input())
x = input().split()

count = 0

for i in range(5):
    if int(x[i]) == n:
        count+= 1    
        
print(count)
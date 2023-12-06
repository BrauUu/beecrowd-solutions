n = int(input())

for _ in range(n):
    l1 = []
    flag = False
    exp = input()
    for char in exp:
        if char in ['(', '[', '{']:
            l1.append(char)
        elif len(l1) > 0:
            if char == ')' and l1.pop() != '(':
                flag = True
                break
            elif char == ']' and l1.pop() != '[':
                flag = True
                break
            if char == '}' and l1.pop() != '{':
                flag = True
                break
        else:
            flag = True
            break
    if len(l1) != 0:
        flag = True
        
    print('S' if flag == False else 'N')
while True:
    s, t = input().split()
    if s == t == '*':
        break
    count = 0
    flag = False
    for i in range(len(s)):
        if s[i] == t[i]:
            if flag:
                count += 1
                flag = False
        else:
            flag = True
            if i == len(s) - 1:
                count += 1
    print(count)
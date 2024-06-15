while True:
    n, m = list(map(int, input().split()))

    if n == m == 0:
        break

    balls = list(map(int, input().split()))
    nums = {*balls}
    flag = False
    i = 1
    for ball in balls:
        nums.add(ball)
        for g in range(i, m):
            diff = abs(ball - balls[g])
            nums.add(diff)
            if len(nums) == n + 1:
                flag = True
                break
        if flag == True:
            break
        i += 1
    
    print('Y' if flag else 'N')
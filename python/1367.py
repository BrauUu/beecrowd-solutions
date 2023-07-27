while True:
    n = int(input())
    if n == 0:
        break
    
    problensUnsolved = []
    totalTime = 0
    solvedCount = 0
    
    for i in range(n):
        problemId, time, res = input().split()
        if res == 'incorrect':
            problensUnsolved.append(problemId)
        elif res == 'correct':
            timesWrong = problensUnsolved.count(problemId)
            if timesWrong > 0:
                totalTime += timesWrong * 20
            totalTime += int(time)
            solvedCount += 1
    
    print(f'{solvedCount} {totalTime}')
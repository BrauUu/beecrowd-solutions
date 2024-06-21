while True:
    try:
        n, g = list(map(int, input().split()))
        diffs = []
        points = 0
        for _ in range(n):
            s, r = list(map(int, input().split()))
            if s > r:
                points += 3
                continue
            diffs.append(abs(r - s))
        diffs.sort()
        remaningGoals = g
        while remaningGoals > 0 and len(diffs) != 0:
            diff = diffs.pop(0)
            goalsToWin = diff + 1
            if goalsToWin <= remaningGoals:
                points += 3
                remaningGoals -= goalsToWin
                continue
            goalsToWin -= remaningGoals
            remaningGoals = 0
            if goalsToWin == 1:
                points += 1
        points += diffs.count(0)
        print(points)
    except EOFError:
        break
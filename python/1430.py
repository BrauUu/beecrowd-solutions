while True:
    x = input()
    if x == '*':
        break
    correctBeatCount = 0
    beatDurationCount = 0
    for char in x:
        if char == '/':
            if beatDurationCount == 1:
                correctBeatCount += 1
            beatDurationCount = 0
        else:
            if char == 'W':
                beatDurationCount += 1
            elif char == 'H':
                beatDurationCount += 0.5
            elif char == 'Q':
                beatDurationCount += 0.25
            elif char == 'E':
                beatDurationCount += 0.125
            elif char == 'S':
                beatDurationCount += 0.0625
            elif char == 'T':
                beatDurationCount += 0.03125
            elif char == 'X':
                beatDurationCount += 0.015625
                
    print(correctBeatCount)
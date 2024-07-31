n = int(input())
l = list(map(int, input().split()))
timesThatAGradeRepeat = {}
maxRepeatedGrade = 0
maxRepeatedTimes = 0
for grade in l:
    v = timesThatAGradeRepeat.get(grade) or 0
    timesThatAGradeRepeat.update({grade: v + 1})
    tempMaxRepeatedTimes = v + 1
    if tempMaxRepeatedTimes >= maxRepeatedTimes:
        if maxRepeatedGrade < grade or tempMaxRepeatedTimes > maxRepeatedTimes:
            maxRepeatedGrade = grade
        maxRepeatedTimes = tempMaxRepeatedTimes
print(maxRepeatedGrade)
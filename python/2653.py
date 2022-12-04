jewelryArr = []
while True:
    try:
        jewelry = input()
        if jewelryArr.count(jewelry) == 0:
            jewelryArr.append(jewelry)
    except:
        print(len(jewelryArr))
        break

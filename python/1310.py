while True:
    try:
        n = int(input())
        costPerDay = int(input())
        daysProfitList = []
        curentProfit = 0
        maxProfit = 0
        for i in range(n):
            x = int(input())
            daysProfitList.append(x)
            if (x - costPerDay) + curentProfit > 0:
                curentProfit += (x - costPerDay)
                if curentProfit > maxProfit:
                    maxProfit = curentProfit       
            else:
                curentProfit = 0
        print(maxProfit)
    except:
        break
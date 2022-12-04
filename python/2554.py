while True:
    try:
        n, d = input().split()
        d = int(d)
        n = int(n)
        
        pizzaDate = [0]
        
        for i in range(d):
            date, p = input().split(" ", 1)
            p = p.split()
            day, month, year = date.split('/')
            day = int(day)
            month = int(month)
            year = int(year)
            
            count = 0
            
            for px in p:
                if int(px) == 1:
                    count += 1
            
            if count == n:
                if pizzaDate[0] == 0 or year <= pizzaDate[2]:
                    if pizzaDate[0] == 0 or month <= pizzaDate[1]:
                        if pizzaDate[0] == 0 or day <= pizzaDate[0]:
                            pizzaDate = [day, month, year]
          
        if pizzaDate[0] == 0:
            print('Pizza antes de FdI')
        else:
            print(f"{pizzaDate[0]}/{pizzaDate[1]}/{pizzaDate[2]}")
            
    except:
        break

        
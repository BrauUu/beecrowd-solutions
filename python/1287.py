import re
while True:
    try:
        n = input()
        s = n
        s = re.sub("[Oo]", "0", s)
        s = re.sub("[l]", "1", s)
        s = re.sub("[, ]", "", s)
        try:
            s = int(s)
            if s >= 0 and s <= 2147483647:
                print(s)
            else:
                raise
        except:
            print('error')
    except:
        break
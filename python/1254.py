while True:
    try:
        tag = input().lower()
        n = input()
        text = input()
        start = 0
        end = 0
        lowerText = text.lower()
        while lowerText.count(tag, end) != 0:
            try:
                start = text.index('<', end)
            except:
                break
            try:
                end = text.index('>', start)
            except:
                end = len(text)
            while True:
                try:
                    lowerText = text.lower()
                    ind = lowerText.index(tag, start, end)
                    text = text[:ind] + n + text[ind+len(tag):]
                    start += len(n)
                    end -= len(tag) - len(n)
                except:
                    break
        print(text)
    except:
        break
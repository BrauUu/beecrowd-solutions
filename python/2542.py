while True:
    try:
        n = int(input())

        m, l = input().split()

        m = int(m)
        l = int(l)

        mCards = []
        lCards = []

        for i in range(m):
            mCards.append(input().split())
            
        for i in range(l):
            lCards.append(input().split())
        
        picks = input().split()
            
        mPick = int(picks[0]) - 1
        lPick = int(picks[1]) - 1

        attribute = int(input()) - 1

        if int(mCards[mPick][attribute]) > int(lCards[lPick][attribute]):
            print("Marcos")
        elif int(mCards[mPick][attribute]) < int(lCards[lPick][attribute]):
            print("Leonardo")
        else:
            print("Empate")
    except:
        break

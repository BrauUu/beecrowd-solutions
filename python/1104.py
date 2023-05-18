while True:
    aliceCardsNum, beatrizCardsNum = list(map(int, input().split()))
    
    if aliceCardsNum == beatrizCardsNum == 0:
        break
    
    aliceCardsSet = set(map(int, input().split()))
    beatrizCardsSet = set(map(int, input().split()))
    
    aliceUniqueCardsCount = len(aliceCardsSet.difference(beatrizCardsSet))
    beatrizUniqueCardsCount = len(beatrizCardsSet.difference(aliceCardsSet))
    
    print(aliceUniqueCardsCount if aliceUniqueCardsCount <= beatrizUniqueCardsCount else beatrizUniqueCardsCount)
n, m = list(map(int, input().split()))

fruits = []
likedFruits = []

for _ in range(n):
    fruits.append(input().lower())

testFruits = list(fruits)

for _ in range(m):
    crypt = input().lower()
    for i in range(0, len(testFruits)):
        fruit = testFruits[i]
        if crypt.find(fruit) != -1:
            testFruits.pop(i)
            likedFruits.append(fruit)
            break
        if crypt[::-1].find(fruit) != -1:
            testFruits.pop(i)
            likedFruits.append(fruit)
            break

for fruit in fruits:
    print(f'Sheldon {"come" if likedFruits.count(fruit) > 0 else "detesta"} a fruta {fruit}')
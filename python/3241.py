n = int(input())

for _ in range(n):
    entry = input()
    if entry.find('=') != -1:
        print("skipped")
        continue
    a = int(entry[:entry.find('+')])
    b = int(entry[entry.find('+')+1:])
    print(a+b)
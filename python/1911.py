while True:
    n = int(input())
    if n == 0:
        break
    originalSignatures = {}
    for _ in range(n):
        name, signature = input().split()
        originalSignatures.update({name: signature})
    m = int(input())
    count = 0
    for _ in range(m):
        name, signature = input().split()
        originalSignature = originalSignatures[name]

        errorCount = 0
        for i in range(len(originalSignature)):
            if originalSignature[i] != signature[i]:
                errorCount += 1
            if errorCount == 2:
                count += 1
                break
    print(count)

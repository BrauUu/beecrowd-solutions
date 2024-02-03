while True:
    n, m = list(map(int, input().split()))
    if n == m == 0:
        break
    servers = []
    count = 0
    for _ in range(n):
        servers.append(input().split()[1:])
    for _ in range(m):
        client = input().split()[1:]
        for server in servers:
            for app in client:
                if server.count(app) > 0:
                    count += 1
                    break
    print(count)
        
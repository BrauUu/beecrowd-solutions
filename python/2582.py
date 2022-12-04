songs = [
    'PROXYCITY',
    'P.Y.N.G.',
    'DNSUEY!',
    'SERVERS',
    'HOST!',
    'CRIPTONIZE',
    'OFFLINE DAY',
    'SALT',
    'ANSWER!',
    'RAR?',
    'WIFI ANTENNAS'
]

n = int(input())

for i in range(n):
    x1, x2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    
    print(songs[x1+x2])
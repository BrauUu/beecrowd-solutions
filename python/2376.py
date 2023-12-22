games = {
    1: ['A', 'B'],
    2: ['C', 'D'],
    3: ['E', 'F'],
    4: ['G', 'H'],
    5: ['I', 'J'],
    6: ['K', 'L'],
    7: ['M', 'N'],
    8: ['O', 'P'],
    9: ['', ''],
    10: ['', ''],
    11: ['', ''],
    12: ['', ''],
    13: ['', ''],
    14: ['', ''],
    15: ['', '']
}

j = 8
for i in range(1, 16):
    game_i_score = list(map(int, input().split()))
    winner = games[i][0] if game_i_score[0] > game_i_score[1] else games[i][1]
    if i == 15:
        print(winner)
        continue
    games[i+j][(i-1)%2] = winner
    j = j - 1 if i % 2 else j
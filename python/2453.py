# x = input()
# z = ''

# for i in range(len(x)):
#     if i == 0:
#         continue
#     elif i == len(x) - 1:
#         z += x[i]
#     else:
#         if x[i] == 'p':
#             if x[i - 1] == 'p' and (x[i + 1] == 'p' or x[i + 1] == ' '):   
#                 z += x[i]
#             else:
#                 continue
#         else:
#             z += x[i]

x = input().split()
y = ''

for i in range(len(x)):
    for g in range(1, len(x[i]), 2):
        y += x[i][g]
    y += ' '

print(y.strip())
# from sys import stdout, stdin

# def quick_sort(arr, left, right, prop):
#     if left < right:
#         pivot = partition(arr, left, right, prop)
#         quick_sort(arr, left, pivot - 1, prop)
#         quick_sort(arr, pivot + 1, right, prop)

# def partition(arr, left, right, prop):
#     pivot = arr[right][prop]
#     i = left - 1
#     for j in range(left, right):
#         if arr[j][prop] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[right] = arr[right], arr[i + 1]
#     return i + 1

# k, n = list(map(int, stdin.readline().split()))
# y, p = list(map(int, stdin.readline().split()))

# mooses = [{'year': y, 'power': p, 'isKarl': True}]
# flag = False

# for _ in range(n+k-2):
#     y, p = list(map(int, stdin.readline().split()))
#     mooses.append({'year': y, 'power': p, 'isKarl': False})

# quick_sort(mooses, 0, len(mooses) - 1, 'year')
# moosesToFight = []

# for i in range(k):
#     moose = mooses.pop(0)
#     moosesToFight.append(moose)

# while True:
#     quick_sort(moosesToFight, 0, len(moosesToFight) - 1,'power')
#     winner = moosesToFight.pop(-1)
#     if winner['isKarl'] == True:
#         stdout.write(f'{winner["year"]}\n')
#         flag = True
#         break
#     if len(mooses) == 0:
#         break
#     moose = mooses.pop(0)
#     moosesToFight.append(moose) 
# if flag == False: 
#     stdout.write('unknown\n')

k, n = list(map(int, input().split()))
y, p = list(map(int, input().split()))
mooses = [{'year': y, 'power': p, 'isKarl': True}]
flag = False

for _ in range(n+k-2):
    y, p = list(map(int, input().split()))
    mooses.append({'year': y, 'power': p, 'isKarl': False})

mooses = sorted(mooses, key=lambda x : x['year'])
moosesToFight = []
for i in range(k):
    moose = mooses.pop(0)
    moosesToFight.append(moose)

while True:
    moosesToFight = sorted(moosesToFight, key=lambda x : x['power'])
    winner = moosesToFight.pop(-1)
    if winner['isKarl'] == True:
        print(winner['year'])
        flag = True
        break
    if len(mooses) == 0:
        break
    moose = mooses.pop(0)
    moosesToFight.append(moose) 
if flag == False: 
    print('unknown')
h, e, a, o, w, x = input().split()

sumGood = int(h) + int(e) + int(a) + int(x)
sumBad = int(o) + int(w)

print('Middle-earth is safe.' if sumGood >= sumBad else 'Sauron has returned.')
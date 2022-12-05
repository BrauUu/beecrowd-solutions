a1 = int(input())
a2 = int(input())
a3 = int(input())

a1Choice = a2 * 2 + a3 * 4
a2Choice = a1 * 2 + a3 * 2
a3Choice = a2 * 2 + a1 * 4

print(min([a1Choice, a2Choice, a3Choice]))
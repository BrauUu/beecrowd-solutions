values = input().split()

sum = 0

for v in values:
    sum += int(v)
    
sub = 9 * int(sum / 9)
sum = sum - sub
    
if sum % 9 == 0:
    print("Rudolph")
elif sum % 8 == 0:
    print("Blitzen")
elif sum % 7 == 0:
    print("Donner")
elif sum % 6 == 0:
    print("Cupid")
elif sum % 5 == 0:
    print("Comet")
elif sum % 4 == 0:
    print("Vixen")
elif sum % 3 == 0:
    print("Prancer")
elif sum % 2 == 0:
   print("Dancer")
elif sum % 1 == 0:
    print("Dasher")
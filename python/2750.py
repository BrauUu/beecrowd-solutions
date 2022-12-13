print('-' * 39)
print('|  decimal  |  octal  |  Hexadecimal  |' )
print('-' * 39)
for n in range(16):
    if n >= 10:
        print(f'|     {n}    |   {oct(n)[2:]}    |       {hex(n)[2:].upper()}       |')
    elif len(oct(n)[2:]) > 1:
        print(f'|      {n}    |   {oct(n)[2:]}    |       {hex(n)[2:]}       |')
    else:
        print(f'|      {n}    |    {oct(n)[2:]}    |       {hex(n)[2:]}       |')
print('-' * 39)
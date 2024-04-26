def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for num, is_prime in enumerate(sieve):
        if is_prime:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    return primes

primes = sieve_of_eratosthenes(10000000)

while True:
    k, l = list(map(int, input().split()))
    if k == l == 0:
        break
    flag = False
    i = 0
    while primes[i] < l:
        item = primes[i]
        if k % item == 0 and (k / item < l or item < l):
            print(f'BAD {item}')
            flag = True
            break
        i += 1
    if flag == False:
        print('GOOD')
        
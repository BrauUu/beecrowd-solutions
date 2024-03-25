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

p = sieve_of_eratosthenes(1000)

n = int(input())
flag = False

for ind in range(len(p)):
    actualNum = p[ind]
    if actualNum > n or ind == len(p) - 1:
        ind -= 1
        while True:
            if p[ind] - 2 == p[ind-1]:
                print(f'{p[ind-1]} {p[ind]}')
                flag = True
                break
            else:
                ind -= 1
        if flag == True:
            break
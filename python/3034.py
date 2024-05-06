n = int(input())

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

def isPrime(x):
    return primes.count(x) > 0

primes = sieve_of_eratosthenes(10000)

for _ in range(n):
    x = int(input()) + 1
    if x % 7 == 0 and x % 2 == 1 and isPrime(x + 2):
        print('Yes')
    else:
        print('No')
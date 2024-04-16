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

n = int(input())
p = sieve_of_eratosthenes(60101)
ind = 0
num = n
while True:
    try:
        ind = p.index(num)
        break
    except:
        num += 1
speed = sum(p[ind:ind+10])
days = 60 * 1000 * 1000 / (speed * 24)
hours = days * 24

print(f'{speed} km/h')
print(f'{int(hours)} h / {int(days)} d')
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def primes_upto(n):
    return [i for i in range(2, n+1) if is_prime(i)]

n = int(input())
print(is_prime(n))
print(primes_upto(n))


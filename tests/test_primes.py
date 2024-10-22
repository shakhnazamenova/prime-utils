import random
from .test_is_prime import is_prime

def primes(M: int) -> list[int]:
    result = [2, 3]
    maxn = M // 6
    n = 1
    while n <= maxn:
        a = 6 * n - 1
        if is_prime(a):
            result.append(a)
        b = 6 * n + 1
        if b >= M:
            break
        else:
            if is_prime(b):
                result.append(b)
        n += 1
    return result

random.seed(100)
prime_numbers = primes(1000)
random.shuffle(prime_numbers)

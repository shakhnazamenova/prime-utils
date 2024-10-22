def is_prime(N: int) -> bool:
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True
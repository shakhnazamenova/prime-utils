from typing import List
import random

def is_prime(N: int) -> bool:
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

def primes(count: int) -> List[int]:
    result = []
    num = 2
    while len(result) < count:
        if is_prime(num):
            result.append(num)
        num += 1
    return result

def checksum(lst: List[int]) -> int:
    control_sum = 0
    for element in lst:
        control_sum += element
        control_sum = (control_sum * 113) % 10000007
    return control_sum

def generate_and_process_primes() -> int:
    prime_numbers = primes(1000)
    random.seed(100)  
    random.shuffle(prime_numbers)
    result = checksum(prime_numbers)
    return result

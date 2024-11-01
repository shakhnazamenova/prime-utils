from typing import List
import random

def is_prime(N: int) -> bool:
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

def generate_prime_number(count: int) -> List[int]:
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

def pipeline() -> int:
    result = checksum([1, 2, 6, 24])
    return result

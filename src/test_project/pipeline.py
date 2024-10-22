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
    # Генерация 1000 первых простых чисел
    prime_numbers = primes(1000)
    
    # Перемешивание списка
    random.seed(100)  # Устанавливаем начальное значение генератора случайных чисел
    random.shuffle(prime_numbers)

    # Вычисление контрольной суммы
    result = checksum(prime_numbers)

    return result

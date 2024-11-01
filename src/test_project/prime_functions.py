from typing import List
import random
import sys 

def is_prime(N: int) -> bool:
    """Проверяет, является ли число простым."""
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

def generate_prime_number(count: int, seed: int) -> List[int]:
    random.seed(seed)  
    result = []
    num = 2

    while len(result) < count:
        if is_prime(num):
            result.append(num)
        num += 1
    
    return result

def checksum(lst: List[int]) -> int:
    """Вычисляет контрольную сумму для списка чисел."""
    control_sum = 0
    for element in lst:
        control_sum += element
        control_sum = (control_sum * 113) % 10000007 
    return control_sum

def pipeline(count: int, seed: int) -> int:
    prime_numbers = generate_prime_number(count, seed)
    
    for number in prime_numbers:
        print(number)
    
    return checksum(prime_numbers)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <count> <seed>")
        sys.exit(1)

    count = int(sys.argv[1])
    seed = int(sys.argv[2])
    result = pipeline(count, seed)
    print(f"Checksum: {result}")

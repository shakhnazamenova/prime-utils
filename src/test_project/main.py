from tests.test_primes import primes
from tests.test_checksum import checksum

def pipeline(N: int) -> int:
    prime_numbers = primes(N)  
    result = checksum(prime_numbers)  
    return result

if __name__ == "__main__":
    N = 1000  
    result = pipeline(N) 
    print(f"Контрольная сумма простых чисел до {N}: {result}")  
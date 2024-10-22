from .test_primes import primes
from .test_checksum import checksum

def pipeline(N: int) -> int:
    prime_numbers = primes(N)  
    result = checksum(prime_numbers)  
    return result
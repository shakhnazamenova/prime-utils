import pytest
from src.test_project.pipeline import primes, checksum

def pipeline(N: int) -> int:
    prime_numbers = primes(N)  #
    result = checksum(prime_numbers)  
    return result  
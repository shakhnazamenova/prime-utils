import pytest
from src.test_project.pipeline import primes

def test_primes():
    assert len(primes(10)) == 10 
    assert primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  
    assert primes(0) == []  
    assert primes(1) == [2]  
import pytest
from src.test_project.pipeline import checksum

def test_checksum_empty():
    assert checksum([]) == 0  
def test_checksum_single_element():
    assert checksum([1]) == 113  
def test_checksum_example():
    assert checksum([1, 2, 6, 24]) == 6012369  

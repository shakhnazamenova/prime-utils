import unittest
from src.test_project.prime_functions import is_prime, checksum, pipeline

class TestIsPrime(unittest.TestCase):

    def test_prime_number(self):
        """Проверяет, что функция возвращает True для простого числа."""
        self.assertTrue(is_prime(7))

    def test_non_prime_number(self):
        """Проверяет, что функция возвращает False для составного числа."""
        self.assertFalse(is_prime(8))

    def test_negative_number(self):
        """Проверяет, что функция возвращает False для отрицательных чисел."""
        self.assertFalse(is_prime(-5))

    def test_edge_case_one(self):
        """Проверяет, что функция возвращает False для числа 1."""
        self.assertFalse(is_prime(1))

class CheckSum(unittest.TestCase):

    def test_null_list(self):
        """Проверяет, что функция возвращает 0 для пустого списка."""
        self.assertEqual(checksum([]), 0)

    def test_checksum(self):
        """Проверяет контрольную сумму для списка [1, 2, 6, 24]."""
        self.assertEqual(checksum([1, 2, 6, 24]), 6012369)

class TestPipeline(unittest.TestCase):

    def test_pipeline(self):
        """Тестирует функцию pipeline с заданными параметрами."""
        result = pipeline(4, 42) 
        self.assertIsInstance(result, int)  

if __name__ == "__main__":
    unittest.main()
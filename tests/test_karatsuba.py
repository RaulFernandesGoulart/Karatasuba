# testes unitários (pytest)
import random
from main import karatsuba

def test_pequenos():
    for a in range(-20, 21):
        for b in range(-20, 21):
            assert karatsuba(a, b) == a * b

def test_grandes():
    nums = [
        (12345678901234567890, 98765432109876543210),
        (10**50 + 12345, 10**40 + 67890),
        (-10**60 + 1, 10**60 - 1),
    ]
    for a, b in nums:
        assert karatsuba(a, b) == a * b

def test_aleatorios():
    for _ in range(50):
        a = random.randint(-10**80, 10**80)
        b = random.randint(-10**80, 10**80)
        assert karatsuba(a, b) == a * b

#!/usr/bin/env python3
from __future__ import annotations
import sys
from typing import Tuple

def _split_number(n: int, m: int) -> Tuple[int, int]:
    pow10 = 10 ** m
    high = n // pow10
    low = n % pow10
    return high, low

def karatsuba(x: int, y: int) -> int:
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)

    if x == 0 or y == 0:
        return 0

    if x < 10 or y < 10:
        return sign * (x * y)

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    x_high, x_low = _split_number(x, m)
    y_high, y_low = _split_number(y, m)

    z0 = karatsuba(x_low, y_low)
    z2 = karatsuba(x_high, y_high)
    z1 = karatsuba(x_low + x_high, y_low + y_high) - z0 - z2

    result = (z2 * (10 ** (2 * m))) + (z1 * (10 ** m)) + z0
    return sign * result

def _cli():
    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    else:
        print("Digite dois números inteiros para multiplicar:")
        a = int(input("Primeiro número: "))
        b = int(input("Segundo número: "))

    resultado = karatsuba(a, b)
    print(f"\nO resultado da multiplicação de {a} x {b} é: {resultado}\n")

if __name__ == "__main__":
    _cli()

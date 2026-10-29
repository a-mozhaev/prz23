"""
Модуль calc_logic.py
Содержит математические функции для калькулятора.
"""

def add(a: float, b: float) -> float:
    """Складывает два числа."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Вычитает второе число из первого."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Умножает два числа."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Делит первое число на второе.
    Вызывает ValueError, если делитель равен 0.
    """
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b

def exponentiation(a: float, b: float) -> float:
    """
    Возводит первое число (основание) в степень второго числа (показатель).
    Вызывает ValueError при попытке возвести 0 в отрицательную степень.
    """
    if a == 0 and b < 0:
        raise ValueError("Ноль нельзя возводить в отрицательную степень!")
    return a ** b

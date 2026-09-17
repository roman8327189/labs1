# lib.py

def factorial(n: int) -> int:
    """Обчислює факторіал невід'ємного цілого числа n рекурсивно."""
    return 1 if n <= 1 else n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """Перевіряє, чи є число n простим."""
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def reverse_string(s: str) -> str:
    """Повертає рядок s у зворотному порядку."""
    return s[::-1]
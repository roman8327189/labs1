# main.py
from lib import factorial, is_prime, reverse_string


def main() -> None:
    """Головна точка входу: демонструє роботу функцій з модуля lib."""
    print(f"5! = {factorial(5)}")
    print(f"Чи просте число 17? {is_prime(17)}")
    print(f"Розвернутий рядок 'DevOps': {reverse_string('DevOps')}")


if __name__ == "__main__":
    main()
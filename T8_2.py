import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Аналізує текст і повертає генератор усіх дійсних чисел, знайдених у ньому.
    Числа мають бути відокремлені пробілами.
    """
    # Розбиваємо текст на окремі слова за пробілами
    words = text.split()
    
    for word in words:
        try:
            # Спробуємо перетворити слово на дійсне число (float)
            number = float(word)
            # Якщо вдалося, повертаємо його через yield
            yield number
        except ValueError:
            # Якщо слово не є числом, просто ігноруємо його
            continue

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Обчислює загальний прибуток, підсумовуючи числа, які надає генератор.
    """
    total = 0.0
    # Викликаємо функцію-генератор, яку ми отримали як аргумент
    for number in func(text):
        total += number
    return total

# --- Приклад використання ---
if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    
    # Передаємо generator_numbers як аргумент (функція вищого порядку)
    total_income = sum_profit(text, generator_numbers)
    
    # Виводимо результат, округлений до 2 знаків після коми (для точності)
    print(f"Загальний дохід: {total_income:.2f}")

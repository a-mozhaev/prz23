"""
Главный модуль приложения Калькулятор.
Отвечает за взаимодействие с пользователем.
"""
import calc_logic  # Импортируем наш новый модуль

def get_number(prompt: str) -> float:
    """Запрашивает у пользователя число с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

def main():
    print("=== Модульный Калькулятор v2.0 ===")

    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")
    operation = input("Выберите операцию (+, -, *, /, **): ")

    try:
        if operation == '+':
            result = calc_logic.add(num1, num2)
        elif operation == '-':
            result = calc_logic.subtract(num1, num2)
        elif operation == '*':
            result = calc_logic.multiply(num1, num2)
        elif operation == '/':
            result = calc_logic.divide(num1, num2)
        elif operation == '**':
            result = calc_logic.exponentiation (num1, num2)
        else:
            print("Неизвестная операция!")
            return

        print(f"Результат: {result}")

    except ValueError as e:
        print(f"Ошибка вычисления: {e}")

if __name__ == "__main__":

    main()


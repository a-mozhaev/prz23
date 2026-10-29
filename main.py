"""
Главный модуль приложения Калькулятор.
Отвечает за взаимодействие с пользователем.
"""
import calc_logic

def get_number(prompt: str) -> float:
    """Запрашивает у пользователя число с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

def main():
    print("=== Модульный Калькулятор v2.0 ===")

    # 1. Сначала запрашиваем первое число
    num1 = get_number("Введите число (или первое число для парных операций): ")
    # 2. Запрашиваем операцию
    operation = input("Выберите операцию (+, -, *, /, **, sqrt): ").strip()

    try:
        # 3. Обрабатываем операцию (вычисоление корня), где второе число не нужно
        if operation.lower() == 'sqrt':
            result = calc_logic.square_root(num1)
            print(f"Результат: √{num1} = {result}")
            return

        # 4. Если операция требует второго числа, запрашиваем его
        if operation in ('+', '-', '*', '/', '**'):
            num2 = get_number("Введите второе число: ")
        else:
            print("Неизвестная операция!")
            return

        # 5. Выполняем парные операции
        if operation == '+':
            result = calc_logic.add(num1, num2)
        elif operation == '-':
            result = calc_logic.subtract(num1, num2)
        elif operation == '*':
            result = calc_logic.multiply(num1, num2)
        elif operation == '/':
            result = calc_logic.divide(num1, num2)
        elif operation == '**':
            result = calc_logic.exponentiation(num1, num2)

        print(f"Результат: {result}")

    except ValueError as e:
        print(f"Ошибка вычисления: {e}")

if __name__ == "__main__":
    main()

"""
Главный модуль приложения Калькулятор.
Отвечает за взаимодействие с пользователем.
"""
import calc_logic
import db_manager 

def get_number(prompt: str) -> float:
    """Запрашивает у пользователя число с обработкой ошибок."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

def perform_calculation():
    """Запрашивает данные, выполняет вычисление и сохраняет в БД."""
    # 1. Сначала запрашиваем первое число
    num1 = get_number("Введите число (или первое число для парных операций): ")
    # 2. Запрашиваем операцию
    operation = input("Выберите операцию (+, -, *, /, **, sqrt): ").strip()

    try:
        # 3. Обрабатываем операцию (вычисление корня), где второе число не нужно
        if operation.lower() == 'sqrt':
            result = calc_logic.square_root(num1)
            # Формируем строку выражения для корня
            expression = f"sqrt({num1})"
            print(f"Результат: √{num1} = {result}")

        # 4. Если операция требует второго числа, запрашиваем его
        elif operation in ('+', '-', '*', '/', '**'):
            num2 = get_number("Введите второе число: ")

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

            # Формируем строку выражения для парных операций
            expression = f"{num1} {operation} {num2}"
            print(f"Результат: {result}")

        else:
            print("Неизвестная операция!")
            return  # Выход из функции вычисления обратно в меню

        # Сохраняем в базу данных
        db_manager.save_record(expression, result)

    except ValueError as e:
        print(f"Ошибка вычисления: {e}")

def show_history():
    """Показывает последние 10 записей из истории."""
    history = db_manager.get_history(10)

    if not history:
        print("История пуста.")
        return

    print("\n--- История вычислений ---")
    for record in history:
        print(f"  [{record[3]}] {record[1]} = {record[2]}")

def main():
    print("=== Модульный Калькулятор v3.0 (с историей) ===")

    # Инициализируем базу данных при запуске
    db_manager.init_db()

    while True:
        print("\n--- Меню ---")
        print("1. Выполнить вычисление")
        print("2. Показать историю (последние 10)")
        print("3. Очистить историю")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == '0':
            print("До свидания!")
            break
        elif choice == '1':
            perform_calculation()
        elif choice == '2':
            show_history()
        elif choice == '3':
            db_manager.clear_history()
            print("История очищена.")
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

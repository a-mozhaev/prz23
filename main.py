
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

    num1 = get_number(
        "Введите число (или первое число для парных операций): "
    )

    operation = input(
        "Выберите операцию (+, -, *, /, %, **, sqrt, absdiff): "
    ).strip()

    try:
        if operation.lower() == 'sqrt':
            result = calc_logic.square_root(num1)
            expression = f"sqrt({num1})"

            print(f"Результат: √{num1} = {result}")

        elif operation in ('+', '-', '*', '/', '%', '**', 'absdiff'):
            num2 = get_number("Введите второе число: ")

            if operation == '+':
                result = calc_logic.add(num1, num2)
            elif operation == '-':
                result = calc_logic.subtract(num1, num2)
            elif operation == '*':
                result = calc_logic.multiply(num1, num2)
            elif operation == '/':
                result = calc_logic.divide(num1, num2)
            elif operation == '%':
                result = calc_logic.modulo(num1, num2)
            elif operation == '**':
                result = calc_logic.exponentiation(num1, num2)
            elif operation == 'absdiff':
                result = calc_logic.absolute_difference(num1, num2)

            expression = f"{num1} {operation} {num2}"
            print(f"Результат: {result}")

        else:
            print("Неизвестная операция!")
            return

        # Сохраняем вычисление в базу данных
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


def show_statistics():
    """Показывает статистику всех вычислений."""

    stats = db_manager.get_statistics()

    print("\n--- Статистика вычислений ---")

    if stats["total"] == 0:
        print("История вычислений пуста.")
        return

    print(f"Общее количество вычислений: {stats['total']}")
    print(f"Среднее значение результатов: {stats['average']:.2f}")
    print(f"Максимальное значение: {stats['max']}")
    print(f"Минимальное значение: {stats['min']}")


def show_search_history():
    """Ищет вычисления по ключевому слову."""

    keyword = input(
        "Введите число или часть выражения для поиска: "
    ).strip()

    if not keyword:
        print("Ошибка: поисковый запрос не может быть пустым.")
        return

    records = db_manager.search_history(keyword)

    if not records:
        print(f"По запросу '{keyword}' ничего не найдено.")
        return

    print(f"\n--- Результаты поиска: {keyword} ---")
    print(f"Найдено записей: {len(records)}")

    for record in records:
        print(f"  [{record[3]}] {record[1]} = {record[2]}")


def main():
    print("=== Модульный Калькулятор v3.0 (с историей) ===")

    db_manager.init_db()

    while True:
        print("\n--- Меню ---")
        print("1. Выполнить вычисление")
        print("2. Показать историю (последние 10)")
        print("3. Очистить историю")
        print("4. Показать статистику")
        print("5. Поиск по истории")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

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

        elif choice == '4':
            show_statistics()

        elif choice == '5':
            show_search_history()

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()


try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

except ValueError:
    print("Ошибка: необходимо ввести число!")

else:
    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == "+":
        print("Результат:", num1 + num2)

    elif operation == "-":
        print("Результат:", num1 - num2)

    elif operation == "*":
        print("Результат:", num1 * num2)

    elif operation == "/":
        if num2 == 0:
            print("Ошибка: на ноль делить нельзя! По крайней мере пока ;-)")
        else:
            print("Результат:", num1 / num2)

    else:
        print("Ошибка: неизвестная операция!")

print("Добро пожаловать в калькулятор!")
print("1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Возведение в степень")
actionNumber = int(input("Введите кол-во действий, которые хотите выполнить: "))
firstNumber = float(input("Введите первое число: "))
i = 1
while i <= actionNumber:
    secondNumber = float(input("Введите второе число: "))
    action = int(input("Введите действие: "))
    if action == 1:
        firstNumber = firstNumber + secondNumber
        print(f"Ответ равен {firstNumber}")
    elif action == 2:
        firstNumber = firstNumber - secondNumber
        print(f"Ответ равен {firstNumber}")
    elif action == 3:
        firstNumber = firstNumber * secondNumber
        print(f"Ответ равен {firstNumber}")
    elif action == 4:
        if firstNumber == 0 or secondNumber == 0:
            print("На ноль делить нельзя!!!")
            i -= 1
        else:
            firstNumber = firstNumber / secondNumber
            print(f"Ответ равен {firstNumber}")
    elif action == 5:
        firstNumber = firstNumber ** secondNumber
        print(f"Ответ равен {firstNumber}")
    else :
        print("Введите другое действие.")
        i -= 1
    i += 1

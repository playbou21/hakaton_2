# Задание 1:
    # Нужно создать обычный калькулятор состоящий из знаков +,-,*,/
    # 1. У пользователя просят выбрать знак
    # 2. Просят ввести 1-ое число
    # 3. Просят ввести 2-ое число
    # 4. Вывести результат
    # 5. После результата спросить у пользователя хочет он закончить или нет, 
    # если нет то калькулятор должен запускатся сначала
    # 6. Учесть то что деление на ноль невозможно
print("Вы открыли калькулятор.")
x = int(input('Введите первое чиcло > '))
while True:
    y = input("Введите тип операции > ")
    z = int(input("Ведите второе чиcло > "))
    print(x, y, z, "=", end=" ")
    if y == '+':
        x = x + z
    elif y == '-':
        x = x - z
    elif y == '*':
        x = x * z
    elif y == '/' and z != 0:
        x = x / z
    else:
        print("Не знаю такой операции")
        continue   
    print(x)
    print("Продолжить работу - 1")
    print("Закончить работу - 2")
    print("Начать заново - 3")
    ans = int(input("> "))
    if ans == 1:
        continue
    if ans == 3:
        x = int(input('Введите первое чило > '))
        continue
    if ans == 2:
        break
    else:
        break

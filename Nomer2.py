num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))
max = num1
if num2 > max:
    max = num2
if num3 > max:
    max = num3
print("Самое большое число - ", max)
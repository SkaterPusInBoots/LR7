num = int(input("Введите целое число больше 1: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "не является простым числом")
            break
    else:
        print(num, "является простым числом")
else:
    print("Число должно быть больше 1")
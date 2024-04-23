s = int(input("Введите неотрицательное число: "))
fact = 1
while s > 1:
    fact *= s
    s -= 1
print(fact)
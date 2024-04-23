def sum(numList):
    Sum = 0
    for i in numList:
        Sum = Sum + i
    return Sum
num = list(map(int, input('Введите числа через пробел: ').split()))
print(sum(num))
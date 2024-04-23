strok = int(input('Сколько будет строк? '))
glas = 0
sogl = 0
allGls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
count = 0
while strok > count:
    litr = input()
    for i in litr:
        if i.isalpha():
            if i in allGls:
                glas += 1
            else:
                sogl += 1
    count += 1

print('Кол-во гласных:', glas)
print('Кол-во согласных:', sogl)
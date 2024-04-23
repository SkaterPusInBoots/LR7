def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)
tixt = input('Введите текст: ')
if(is_palindrome(tixt)):
    print('это палиндром')
else:
    print ('Это не палиндром')
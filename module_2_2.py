a = input('Введите число 1: ')
b = input('Введите число 2: ')
c = input('Введите число 3: ')
if a == b == c:
    print(3)
elif a == b != c or a == c != b or c == b != a:
    print(2)
else:
    print(0)
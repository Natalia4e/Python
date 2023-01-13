# на вход программе подается число n . Программа печатает численный треугольник. Исп-ем вложенные циклы
iteration = int(input("Введите число: "))
for i in range(1,iteration+1):
    for k in range(i):
        print(i, end='')
    print()

        
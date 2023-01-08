#3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Без использования встроенной функции преобразования, без строк.
#Без использования встроенной функции преобразования, без строк.
# разобрать число на числа , 


list = []
decimal_number = int(input('Введите десятичное число: '))
print(decimal_number)
while decimal_number != 0:
    list.append(decimal_number % 2)
    decimal_number = decimal_number // 2
print(list)
#2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# если длина нечетная значение с парами перемножаем , число без пары НЕ умножаем само на себя, выводим одно его

from random import sample

def multiply_number (amount):
    new_list = sample(range(1,amount+1), k=amount)
    print(new_list)
    i = 0
    multiply_list = []
    while i <= amount-i-1:
        print(new_list[i],new_list[amount-i-1])
        if i == amount - i - 1:
            multiply_list.append(new_list[i])
        else:
             multiply_list.append(new_list[i]*new_list[amount-i-1])
        i = i+1
    print(multiply_list)
        
            
result = multiply_number(int(input('Введите количество чисел - ')))
print(result)
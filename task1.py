#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def sum_number (amount):
    new_list = sample(range(1,amount+1), k=amount)
    print(new_list)
    sum = 0
    for i in range(amount):
        if i % 2 == 0:
            sum += new_list[i]
    print(f"Сумма элементов, на нечетных позициях равна: {sum}")

result = sum_number(int(input('Введите количество чисел - ')))

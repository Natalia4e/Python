# Задайте список, состоящий из произвольных чисел, количество задает пользователь.
# Напишите программу, определяющую присутствует ли в заданном списке число , подученное от пользователя

from random import sample
def find_number (amount, user_number):
    new_list = sample(range(1,amount+1), k=amount)
    print(new_list)
    if user_number in new_list:
        return 'yes'
    return 'no'


result = find_number(int(input('Enter amount - ')), int(input('Enter the desired number-')))
print(result)
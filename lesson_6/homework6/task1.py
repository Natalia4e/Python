# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension. 

from random import choices

amount = int(input("Введите необходимое количество чисел: "))
new_list = choices(range(1,amount+1), k=amount)
print(new_list)

def find(any_list):
    result_list = []
    for i in range(1, len(any_list)):
        if any_list[i] > any_list[i-1]:
            result_list.append(any_list[i])
    return result_list

print(find(new_list))
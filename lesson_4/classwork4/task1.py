#Задайте строку из набора чисел. Напишите программу, которая покажет наибольшее и наименьшее число.
# Вкачестве разделителя используйте пробел

def check ():
    enter_list = input("Введите числа через пробел: ").split()
    new_list = []
    for i in range(len(enter_list)):
        enter_list[i] = enter_list[i].strip("!,;")
        if enter_list[i].isdigit:
            new_list.append(enter_list[i])
    print(new_list)
    return new_list


def max_min_finder(any_list):
    if any_list:
        return max(any_list, key=int), min(any_list, key=int)
    return []
    

print(max_min_finder(check()))
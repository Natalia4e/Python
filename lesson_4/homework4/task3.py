#3. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности в том же порядке.


def check ():
    enter_list = input("Введите числа через пробел: ").split()
    new_list = []
    for i in range(len(enter_list)):
        enter_list[i] = enter_list[i].strip("!,;")
        if enter_list[i].isdigit:
            new_list.append(enter_list[i])
    print(new_list)
    return new_list


def identical_numb(any_list):
    temp = []
    for x in any_list:
        if x not in temp:
            temp.append(x)
    any_list= temp
    print(temp)

print(identical_numb(check()))

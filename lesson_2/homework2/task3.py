# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

num_list = []
sum_nums = 0
n = int(input("Введите число: "))
for i in range (1, n+1):
    result = round((1+1/i)**i, 3)
    num_list.append((1+1/i)**i)
    sum_nums += result
print(num_list)
print(sum_nums)

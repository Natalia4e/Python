# Программа принимает на вход 5 чисел и находит максимальное из них. Только положительные !!
max_num = 0
for i in range(5):
    num = int(input())
    if num > max_num:
        max_num = num
print(max_num)

# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in 100
# out [20, 21, 40, 42, 60, 63, 80, 84, 100]

c =int(input("Введите число больше 20"))
res = res = [x for x in range(20, c+1, 1) if x % 20 == 0  or x % 21 == 0 ]
print(res)
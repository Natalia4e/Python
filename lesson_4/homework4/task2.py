#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = int(input("Задайте натуральное число N: "))
i = 2
new_list = []
while i <= N:
    if N%i == 0:
         new_list.append(i)
         N = N//i
         i = 2
    else:
        i=i+1
print(f"Простые множители заданного числа = {new_list}")


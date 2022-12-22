# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
num_list = [1]
n = int(input("Введите число: "))
for i in range (1,n):
    num_list.append(num_list[i-1]*(i+1))
print(num_list)
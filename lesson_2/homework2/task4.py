#4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

N = int(input())
num_list = []
for i in range (-N, N+1):
    num_list.append(i)

print(num_list)

a = int(input("Введите позицию"))
b = int(input("Введите позицию"))
a = int(a)-1
b = int(b)-1

res = num_list[a]*num_list[b]
print (f"Position one: {a+1}\n Position two: {b+1}\n  Result {res}")
#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
from math import trunc

n = float(input("Введите число: "))
sum = 0
if (n < 0):
    n = n * (-1)
while n != trunc(n):
    n = n * 10
while (n > 0):
    count = n % 10
    sum = sum + count 
    n = n//10
print (sum)

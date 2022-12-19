# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

day_of_week = int(input("Введите цифру дня недели: "))
if (day_of_week >= 1 and day_of_week <= 5):
    print ('Workday')
elif (day_of_week >= 6 and day_of_week <= 7):
    print ('Weekend')
else:
    print ('Incorrect input, plese check')
# Найдите корни квадратнго уровнения Ax2+bx+c=0 с помощью модуля. Запросите значения a,b,c 3 раза.
# уровнения и корни запишите в файл
from math import sqrt

def find_r(a, b, c):
    D =  b**2 - 4*a*c
    with open("Discr.txt", "a", encoding="utf-8") as my_f:
        my_f.write(F"{a}Х²  + {b} x + {c} = 0\n")
        if D > 0 :
            x1 = (-b - sqrt(D))/(2*a)
            x2 = (-b + sqrt(D))/(2*a)
            my_f.write(f"{x1, x2}\n")
        elif D == 0 :
            x = -b/(2*a)
            my_f.write(f"{x}\n")
        else:
            my_f.write("Корней нет\n")

find_r(3, 8, 2)



#1. Вычислить число c заданной точностью d 8.98785




from decimal import Decimal

N = input('Введите число:')
d = Decimal(N)
d = d.quantize(Decimal("1.0000"))
print(d)
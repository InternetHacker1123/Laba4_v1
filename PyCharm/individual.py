# Пусть основания трапеции равны a и b, а угол при большем основании равен α. Тогда площадь трапеции S вычисляется по формуле:

# S = ((a + b) / 2) * h

# где h - высота трапеции, которую можно найти по формуле:

# h = (b - a) / 2 * tan(α/2)

# Таким образом, полная формула для вычисления площади трапеции будет выглядеть так:

# S = ((a + b) / 2) * ((b - a) / 2 * tan(α/2))

import math

osn1 = int(input("osn 1="))
osn2 = int(input("osn 2="))

ygol = int(input("ygol pri bol'shem osnovanii = "))

print(f"S = {((osn1 + osn2)/2) * ((osn2 - osn1)/2 * math.tan(ygol/2))}")
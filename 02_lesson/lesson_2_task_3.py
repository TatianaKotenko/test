import math


def square(number):
    return math.ceil(number*number)


square_area = int(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {square(square_area)}")

# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

num = int(input("Введите целое число от 1 до 7:  "))
if num > 0 and num <= 5:
    print(" не выходной")
elif num == 6 or num == 7:
    print(" выходной ")
else:
    print(" Вы ввели неверное число, введите число от 1 до 7")

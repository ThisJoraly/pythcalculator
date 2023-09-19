# Калькулятор от артёма из п5-22
import math
import sys

print("Калькулятор ОАиП")
while True:
    print("Введите знак действия (+, -, *, /, **, sqrt, !, sin, cos, tan)")
    print("Напишите \"q\" для выхода")
    # v значит знак действия, a - первое число, b - второе число
    v = str(input(""))
    if not (v == "q"):
        try:
            a = float(input("Введите первое число: "))
        except(ValueError):
            print("Введите число!")
            continue
    if not (v == "sqrt" or v == "!" or v == "sin" or v == "cos" or v == "tan" or v == "q"):
        try:
            b = float(input("Введите второе число: "))
        except(ValueError):
            print("Введите число!")
            continue
    match (v):
        case "+": print(a + b)
        case "-": print(a - b)
        case "*": print(a * b)
        case "/":
            try:
                print(a / b)
            except ZeroDivisionError:
                print("На ноль делить нельзя!")
        case "**": print(a ** b)
        case "sqrt": print(math.sqrt(a))
        case "!":
            print(math.factorial(int(a)))
        case "sin": print(math.sin(a))
        case "cos": print(math.cos(a))
        case "tan": print(math.tan(a))
        case "q": break
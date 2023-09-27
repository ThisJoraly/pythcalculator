# Калькулятор от артёма из п5-22
import math
v = ""
############################################################
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def modify(a, b):
    return a * b


def divide(a, b):
    return a / b


def pow(a, b):
    return a ** b


def sqrt(a):
    return math.sqrt(a)


def factorial(a):
    return math.factorial(int(a))


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def tan(a):
    return math.tan(a)
############################################################
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
        case "+": print(add(a, b))
        case "-": print(subtract(a, b))
        case "*": print(modify(a, b))
        case "/":
            try:
                print(divide(a, b))
            except ZeroDivisionError:
                print("На ноль делить нельзя!")
        case "**": print(pow(a, b))
        case "sqrt":
            try:
                print(sqrt(a))
            except ValueError:
                print(f"Нельзя найти корень данного числа: {a}")
        case "!":
            try:
                print(factorial(a))
            except(ValueError):
                print("Введите другое число для факториала")
                continue
        case "sin": print(sin(a))
        case "cos": print(cos(a))
        case "tan": print(tan(a))
        case "q": break

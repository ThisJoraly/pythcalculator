def rectangle_area(width, height):
    return height * width
def is_even(number):
    if number % 2 == 0:
        return f"Число {number} четное"
    else:
        return f"Число {number} нечетное"
def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

print(rectangle_area(10,200))
print(is_even(4))
print(is_even(5))
print(sum_digits(1234))
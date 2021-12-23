#does not work because multiplication takes only two parameters
# def mul(x, y, k, u):


def mul(*numbers):
    total = 1
    for i in numbers:
        total *= i
    return total        
print(mul(9, 8, 9, 7))
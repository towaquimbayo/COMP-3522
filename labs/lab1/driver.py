def my_sum(a, b):
    """
    Adds two numbers together
    :param a: first integer value
    :param b: second integer value
    :precondition: a and b must be integers
    :return: sum of a and b
    """
    return a + b


def my_subtract(a, b):
    """
    Subtracts two numbers
    :param a: first integer value
    :param b: second integer value
    :precondition: a and b must be integers
    :return: difference of a and b
    """
    return a - b


def my_multiply(a, b):
    """
    Multiplies two numbers
    :param a: first integer value
    :param b: second integer value
    :precondition: a and b must be integers
    :return: product of a and b
    """
    return a * b


def my_divide(a, b):
    """
    Divides two numbers
    :param a: first integer value
    :param b: second integer value
    :precondition: a and b must be integers
    :return: quotient of a and b
    """
    return a / b


num_a = int(input("enter first number: "))
num_b = int(input("enter second number: "))
print("1 to add")
print("2 to subtract")
print("3 to multiply")
print("4 to divide")
option = int(input())
if option == 1:
    print(my_sum(num_a, num_b))
elif option == 2:
    print(my_subtract(num_a, num_b))
elif option == 3:
    print(my_multiply(num_a, num_b))
elif option == 4:
    print(my_divide(num_a, num_b))

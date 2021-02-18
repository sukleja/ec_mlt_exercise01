# 1
def name_age():
    name = input("Enter name: ")
    age = input("Enter age: ")
    print("Hello " + name + " Your age is: " + age)


# 2
def swap_integer():
    num1 = input("Enter first Number x: ")
    num2 = input("Enter second Number y: ")

    print("x: " + num1)
    print("y: " + num2)

    temp = num1
    num1 = num2
    num2 = temp

    print("After swap:")
    print("x: " + num1)
    print("y: " + num2)


# 3
def check_numbers(num1: int, num2: int):
    if num1 % 6 == 0 or num2 % 6 == 0:
        if num1 % 10 == 0 and num2 % 10 == 0:
            return True
        else:
            return False
    else:
        return False


# 4
def sum_up(num1: int, num2: int):
    sum: int = int(0)
    if num2 < num1:
        print("Second number must be greater than the first")
    if num1 > 0 and num2 > 0:
        end: int = (num2 - num1) + 1
        for i in range(end):
            sum += num1 + i
    print("The sum up is: " + str(sum))
    return sum


# 5
def min_int(num1: int, num2: int, num3: int):
    smallest = 0
    if num1 < num2 and num1 < num3:
        smallest = num1
    elif num2 < num1 and num2 < num3:
        smallest = num2
    else:
        smallest = num3
    return smallest


# 6
def check_string(text: str):
    if text.lower().startswith("a") or text.lower().endswith("a"):
        return True
    else:
        return False


# 7
def sum_floats(num1: float, num2: float):
    sum = 0.0

    if isinstance(num1, float) and isinstance(num1, float):
        sum = num1 + num2
        return sum
    else:
        print("Only floats allowed")
        return 0.0


if __name__ == '__main__':
    # name_age()
    # swap_integer()
    print(check_numbers(60, 10))
    sum_up(3, 9)
    print(min_int(200, 700, 31000))
    print(check_string("ANT"))
    sum_floats(1.0, 2.0)

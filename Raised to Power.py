base_num = int(input("Base Number: "))
exponent = int(input("Exponent: "))


def rtb():
    result = 1
    for index in range(exponent):
        result = result * base_num
    return result


print(rtb())

base_num = ""
exponent = ""


def rtb():
    result = 1
    for index in range(exponent):
        result = result * base_num
    return result


while base_num == "":
    try:
        base_num = int(input("Base Number: "))
        exponent = int(input("Exponent: "))
    except ValueError:
        print("*sigh* don't act up")


print(rtb())

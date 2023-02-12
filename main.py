def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Harshit')


# str
def strSwap(str):
    length = len(str)
    if length == 0 and length == 1:
        return str
    output = ""
    temp = ""
    for i in range(length):
        temp += str[i]
        if i % 2 == 1:
            output += swap(temp)

    print(output)
    return output


def swap(str):
    return str[::-1]


strSwap("abcdefg")


def strSwap2(str):
    length = len(str)
    if length == 0 and length == 1:
        return str
    output = ""
    for i in range(length):
        if i % 2 == 0:
            if i == length - 1:
                output += str[i]
            else:
                output += str[i + 1]
        else:
            output += str[i - 1]

    print(output)
    return output

strSwap2("abcdefg")


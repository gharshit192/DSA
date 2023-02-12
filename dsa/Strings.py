'''
    Swap string in 2 pairs
    eg - abcd
    output - badc
'''


def strSwap(str):
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


strSwap("abcdefg")

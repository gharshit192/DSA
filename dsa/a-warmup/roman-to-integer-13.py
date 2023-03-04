'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''


def romanToInt(s):

    dataSet = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    # s = list(s)
    output = 0
    s = s.replace("IV","IIII").replace("XL","XXXX").replace("CD","CCCC").replace("CM","DCCCC").replace("XC","LXXXX").replace("IX","VIIII")
    print(s)

    for i in range(len(s)):
        output +=dataSet.get(s[i])

    print(output)
    return output


romanToInt("MCMXCIV")


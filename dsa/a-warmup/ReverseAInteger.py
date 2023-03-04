'''
    Reverese an Integer
    Modulus No doesn't handle a negative no
     https://leetcode.com/problems/reverse-integer/
'''

# Time Complexity - O(n)
def reverse(val):
    integerRange = 2**31
    output = 0
    isNeg = False
    if val < 0:
        isNeg = True

    originalNumber = abs(val)
    while originalNumber :
        lastDigit = originalNumber % 10
        output = (10 * output) + lastDigit
        originalNumber = originalNumber // 10

    if isNeg:
        output = output * (-1)

    if output < -integerRange or output > integerRange:
        output = 0
    return output

for x in [
    1239876546789098765
]:
    reverse(x)

'''
    1. revere a string and compare
    2. two pointer technique compare and check
'''


def isValidPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False

    return True


def isValidPalindrome_2(s):
    low = 0
    high = len(s) -1

    while low < high:
        if not s[low].isalnum():
            low += 1
            continue
        if not s[high].isalnum():
            high -= 1
            continue
        if s[low].lower() != s[high].lower():
            return False
        low, high = low + 1, high - 1

    return True


output = isValidPalindrome_2("A man, a plan, a canal: Panama")
print(output)

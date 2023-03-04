'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting
 from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater
than or equal to k characters,then reverse the first k characters and leave the other as original.

'''


def reverseStr(s, k):
    finalOutput = ""
    if k == 1:
        return s

    def rev(key, subStr):
        output = ""
        for i in range(key - 1, - 1, -1):
            output += subStr[i]
        output += subStr[key:]
        return output

    lengthOfOriginalStr = len(s)

    if lengthOfOriginalStr < k:
        if lengthOfOriginalStr < k:
            rev = ""
            for i in range(lengthOfOriginalStr - 1, - 1, -1):
                rev += s[i]
            return rev

    twoK = 2 * k

    loopToExecute = lengthOfOriginalStr // twoK
    remainingLength = lengthOfOriginalStr % twoK

    listOfSubSTr = []
    startIndex = 0
    for i in range(0, loopToExecute):
        subStr = ""
        if startIndex == 0:
            subStr = s[:twoK]
        else:
            subStr = s[startIndex: twoK]

        listOfSubSTr.append(subStr)
        startIndex += twoK
        twoK += twoK

    for subStr in listOfSubSTr:
        finalOutput += rev(k, subStr)

    if remainingLength >= k:
        finalOutput += rev(k, s[(lengthOfOriginalStr - remainingLength):])
    else:
        finalOutput += s[(lengthOfOriginalStr - remainingLength):]

    print(finalOutput)
    return finalOutput


output = reverseStr("abcdefghijk",4 )
print(output)

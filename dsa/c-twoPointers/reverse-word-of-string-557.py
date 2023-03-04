def reverseWord(word, low, high):
    while low < high:
        word[low], word[high] = word[high], word[low]
        low, high = low + 1, high - 1
    return word


def reverseWords(s):

    wordList = str.split(" ")
    finalStr = ""
    for word in wordList:
        finalStr += reverseWord(word) + " "
    print(finalStr)
    return finalStr


# reverseWords("Let's take LeetCode contest")

def reverseWordsWithoutSplit(s):
    def reverseWord(word, low, high):
        while low < high:
            word[low], word[high] = word[high], word[low]
            low, high = low + 1, high - 1
        return word
    length = len(s)
    print(s)

    s = list(s)
    start = 0
    for end in range(length+1):
        if end == length or s[end] == " ":
            reverseWord(s, start, end - 1)
            start = end + 1
    return "".join(s)

def reverseWordsWithoutSplit(s):
    length = len(s)
    s = list(s)
    start = 0
    for end in range(length + 1):
        if end == length or s[end] == " ":
            low = start
            high = end - 1
            while low < high:
                s[low], s[high] = s[high], s[low]
                low, high = low + 1, high - 1

            start = end + 1
    return "".join(s)

for string in [
    "Let's take LeetCode contest"
]:
    print(reverseWordsWithoutSplit(string))

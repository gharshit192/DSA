'''
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
Input: s = "leetcode"
Output: 0
Input: s = "loveleetcode"
Output: 2
'''
from collections import Counter


# T n , s =1 ----> as we have max letters is 26 so that can be easily ignore so space will be constant
def firstUniqueChar(s):
    n = len(s)
    freq = Counter(s)
    for i in range(n):
        if freq[s[i]] == 1:
            return i
    return -1


for s in ["leetcode", "loveleetcode", "aabb"]:
    print(firstUniqueChar(s))

# T n^2 , s =1
def unique(s):
    n = len(s)
    for i in range(n):
        isRepeated = False
        for j in range(n):
            if i != j and s[i] == s[j]:
                isRepeated = True
                break
        if not isRepeated:
            return i
    return -1


for s in ["leetcode", "loveleetcode", "aabb"]:
    print(unique(s))

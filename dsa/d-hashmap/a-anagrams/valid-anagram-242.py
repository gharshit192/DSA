'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
'''
from collections import Counter


# T- O(n) S(n) -> s(1) only 26 charctaers
def isAnagram(s, t):
    freq_s = Counter(s)
    freq_t = Counter(t)
    if len(s) != len(t):
        return False
    for key in freq_t:
        if key in freq_s and freq_t[key] == freq_s[key]:
            return True
        else:
            return False

for list in [["anagram", "nagaram"], ["rat", "car"]]:
    print(isAnagram(list[0], list[1]))
def isAnagram(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) ==sorted(t)

# T- O(n) S(n) -> s(1) only 26 charctaers
def isAnagram(s, t):
    freq_s = Counter(s)
    freq_t = Counter(t)
    if len(s) != len(t):
        return False

    return freq_s == freq_t


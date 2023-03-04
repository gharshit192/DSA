'''
Given two strings s and p, return an array of all the start indices of p's a-anagrams in s.
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
from collections import Counter


# T n(n-m+1) , S= n(n-m+1)
def findAnagrams(s, p):
    def isAnagram(s, t):
        freq_s = Counter(s)
        freq_t = Counter(t)
        if len(s) != len(t):
            return False
        return freq_s == freq_t

    indexes = []
    n = len(s)
    m = len(p)
    if m > n:
        return indexes
    for i in range(n - m + 1):
        subString = s[i: i + m]
        if isAnagram(p, subString):
            indexes.append(i)

    print(indexes)
    return indexes


findAnagrams("cbaebabacd", "abc")

from typing import List


# Reverse String
def reverseString(self, s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1


# Reverse Integer
def reverse(self, x: int) -> int:
    if x == 0:
        return x
    minus = 0
    if x < 0:
        minus = 1
        x = -x
    ans = 0
    while x > 0:
        ans = ans * 10 + x % 10
        x = x // 10
    if minus == 1:
        ans = -ans
    if -2147483648 < ans < 2147483647:
        return ans
    else:
        return 0


# First Unique Character in a String
def firstUniqChar(self, s: str) -> int:
    dic = {}
    i = 0
    while i < len(s):
        if s[i] in dic:
            dic[s[i]] = -1
        else:
            dic[s[i]] = i
        i += 1
    ans = -1
    for j in dic:
        if dic[j] != -1:
            if ans == -1:
                ans = dic[j]
            else:
                ans = min(ans, dic[j])
    return ans


# Valid Anagram
def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    dic = {}
    i = 0
    while i < len(s):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
        if t[i] in dic:
            dic[t[i]] -= 1
        else:
            dic[t[i]] = -1
        i += 1
    for j in dic:
        if dic[j] != 0:
            return False
    return True


# Valid Palindrome
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    i = 0
    while i < len(s):
        if 47 < ord(s[i]) < 58 or 96 < ord(s[i]) < 123:
            i += 1
        else:
            s = s[:i] + s[i + 1:]
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

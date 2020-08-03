class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        length = len(s)
        while i < length:
            if 47 < ord(s[i]) < 58 or 96 < ord(s[i]) < 123:
                i += 1
            else:
                s = s[:i] + s[i + 1:]
                length -= 1
        i = 0
        j = length - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

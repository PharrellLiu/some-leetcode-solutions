class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        len_s = len(s)
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
        for i in dic:
            if dic[i] != 0:
                return False
        return True

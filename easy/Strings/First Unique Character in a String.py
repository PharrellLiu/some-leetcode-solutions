class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        i = 0
        len_s = len(s)
        while i < len_s:
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                dic[s[i]] = -1
            i += 1
        result = 2 ** 31 - 1
        for i in dic:
            if dic[i] != -1:
                result = min(result, dic[i])
        if result != 2 ** 31 - 1:
            return result
        return -1

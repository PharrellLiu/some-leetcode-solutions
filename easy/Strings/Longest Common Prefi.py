from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPrefix(s1, s2):
            result = ''
            i = 0
            min_len = min(len(s1), len(s2))
            while i < min_len:
                if s1[i] != s2[i]:
                    break
                result += s1[i]
                i += 1
            return result

        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        result = commonPrefix(strs[0], strs[1])
        i = 2
        len_s = len(strs)
        while i < len_s:
            result = commonPrefix(result, strs[i])
            if len(result) == 0:
                break
            i += 1
        return result

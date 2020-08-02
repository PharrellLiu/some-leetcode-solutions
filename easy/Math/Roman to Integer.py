class Solution:
    def romanToInt(self, s: str) -> int:
        dic1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dic2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        result = 0
        len_s = len(s)
        while i < len_s:
            if s[i:i + 2] in dic2:
                result += dic2[s[i:i + 2]]
                i += 2
            else:
                result += dic1[s[i]]
                i += 1
        return result

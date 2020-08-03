class Solution:
    def myAtoi(self, str: str) -> int:
        s = str
        if s == '':
            return 0
        s = s.strip()
        if s == '':
            return 0

        def cal(i):
            res = 0
            while i < len(s):
                if s[i].isdigit():
                    res = res * 10 + int(s[i])
                    i += 1
                else:
                    break
            return res

        result = 0
        if s[0] in '-+':
            minus = 1
            if s[0] == '-':
                minus = -1
            result = minus * cal(1)
        if s[0].isdigit():
            result = cal(0)
        if result < -2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647
        return result

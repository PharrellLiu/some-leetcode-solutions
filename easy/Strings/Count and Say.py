class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = '1'
        new_s = ''
        i = 2
        while i <= n:
            j = 1
            curr_char = s[0]
            count = 1
            len_s = len(s)
            while j < len_s:
                if s[j] != curr_char:
                    new_s += str(count) + curr_char
                    count = 1
                    curr_char = s[j]
                else:
                    count += 1
                j += 1
            new_s += str(count) + curr_char
            s = new_s
            new_s = ''
            i += 1
        return s

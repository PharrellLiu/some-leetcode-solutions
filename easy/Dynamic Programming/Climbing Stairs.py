class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        result = [1, 2]
        i = 3
        while i <= n:
            way = result[0] + result[1]
            result[0] = result[1]
            result[1] = way
            i += 1
        return result[1]

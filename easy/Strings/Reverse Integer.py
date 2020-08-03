class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = int(str(x)[::-1])
        if x <= 0:
            x = -1 * int(str(x * -1)[::-1])

        minx = -2 ** 31
        maxx = 2 ** 31 - 1
        if x not in range(minx, maxx):
            return 0
        return x

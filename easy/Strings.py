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

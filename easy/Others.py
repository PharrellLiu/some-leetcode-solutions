from typing import List


# Number of 1 Bits
def hammingWeight(self, n: int) -> int:
    s = bin(n)
    count = 0
    i = 2
    while i < len(s):
        if s[i] == '1':
            count += 1
        i += 1
    return count


# Hamming Distance
def hammingDistance(self, x: int, y: int) -> int:
    z = x ^ y
    z = bin(z)[2:]
    ans = 0
    for i in z:
        if i == '1':
            ans += 1
    return ans


# Reverse Bits
def reverseBits(self, n: int) -> int:
    n = "{:032b}".format(n)
    return int(n[::-1], 2)


# Pascal's Triangle
def generate(self, numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    ans = [[1], [1, 1]]
    i = 3
    while i <= numRows:
        res = [1 for _ in range(i)]
        j = 1
        while j < len(res) - 1:
            res[j] = ans[-1][j] + ans[-1][j - 1]
            j += 1
        i += 1
        ans.append(res)
    return ans


# Valid Parentheses
def isValid(self, s: str) -> bool:
    stack = []
    i = 0
    while i < len(s):
        stack.append(s[i])
        if len(stack) > 1:
            if (stack[-1] == ']' and stack[-2] == '[') or (stack[-1] == '}' and stack[-2] == '{') or (
                    stack[-1] == ')' and stack[-2] == '('):
                stack.pop()
                stack.pop()
        i += 1
    return len(stack) == 0


# Missing Number
def missingNumber(self, nums: List[int]) -> int:
    i = 0
    ans = 0
    while i < len(nums):
        ans = ans ^ i ^ nums[i]
        i += 1
    return ans ^ len(nums)

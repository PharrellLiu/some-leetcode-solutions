from typing import List


# Climbing Stairs
def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    i = 3
    ans = [1, 2]
    while i < n + 1:
        res = ans[0] + ans[1]
        ans[0] = ans[1]
        ans[1] = res
        i += 1
    return ans[1]
# met in the interview of Bytedance


# Best Time to Buy and Sell Stock
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    minus = 0
    i = 1
    while i < len(prices):
        minus += prices[i] - prices[i - 1]
        if minus < 0:
            minus = 0
        profit = max(minus, profit)
        i += 1
    return profit


# Maximum Subarray
def maxSubArray(self, nums: List[int]) -> int:
    sumNow = 0
    ans = 0
    i = 0
    while i < len(nums):
        sumNow += nums[i]
        if sumNow < 0:
            sumNow = 0
        ans = max(sumNow, ans)
        i += 1
    if ans == 0:
        return max(nums)
    else:
        return ans


# House Robber
def rob(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    i = 2
    ans = [nums[0], max(nums[0], nums[1])]
    while i < len(nums):
        res = max(ans[1], ans[0] + nums[i])
        ans[0] = ans[1]
        ans[1] = res
        i += 1
    return ans[1]

from typing import List


# Jump Game
def canJump(self, nums: List[int]) -> bool:
    if len(nums) == 1:
        return True
    count = 0
    i = 0
    while i < len(nums):
        if count == i + nums[i] and nums[i] == 0:
            return False
        count = max(count, i + nums[i])
        if count >= len(nums) - 1:
            return True
        i += 1
    return True


# Unique Paths
def uniquePaths(self, m: int, n: int) -> int:
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if i - 1 >= 0 and j - 1 < 0:
                dp[i][j] = dp[i - 1][j]
            if j - 1 >= 0 and i - 1 < 0:
                dp[i][j] = dp[i][j - 1]
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]

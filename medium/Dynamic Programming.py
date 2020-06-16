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

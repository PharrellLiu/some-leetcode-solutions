from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        i = 1
        len_nums = len(nums)
        while i < len(nums):
            result ^= nums[i]
            i += 1
        return result

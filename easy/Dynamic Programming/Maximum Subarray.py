from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        curr_sum = 0
        i = 0
        len_nums = len(nums)
        while i < len_nums:
            curr_sum += nums[i]
            if curr_sum < 0:
                curr_sum = 0
            max_sum = max(max_sum, curr_sum)
            i += 1
        if max_sum == 0:
            return max(nums)
        return max_sum

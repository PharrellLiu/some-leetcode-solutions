from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        if len_nums == 1:
            return nums[0]
        if len_nums == 2:
            return max(nums)
        max_amount = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len_nums:
            curr_amount = max(max_amount[0] + nums[i], max_amount[1])
            max_amount[0] = max_amount[1]
            max_amount[1] = curr_amount
            i += 1
        return max_amount[1]

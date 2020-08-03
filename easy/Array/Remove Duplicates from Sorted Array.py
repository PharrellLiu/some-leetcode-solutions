from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        len_nums = len(nums)
        while i < len_nums:
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                len_nums -= 1
            else:
                i += 1
        return len_nums

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        noZero = 0
        len_nums = len(nums)
        while i < len_nums:
            if nums[i] != 0:
                if i == noZero:
                    noZero += 1
                else:
                    temp = nums[i]
                    nums[i] = nums[noZero]
                    nums[noZero] = temp
                    noZero += 1
            i += 1

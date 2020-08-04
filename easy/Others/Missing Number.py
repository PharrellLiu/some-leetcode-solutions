from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_xor = nums[0]
        position_xor = 0
        i = 1
        len_nums = len(nums)
        while i < len_nums:
            num_xor ^= nums[i]
            position_xor ^= i
            i += 1
        return num_xor ^ position_xor ^ len_nums

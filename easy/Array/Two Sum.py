from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        i = 0
        while target - nums[i] not in dic:
            dic[nums[i]] = i
            i += 1
        return [i, dic[target - nums[i]]]

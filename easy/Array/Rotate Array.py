from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        while i < k:
            temp = nums.pop()
            nums.insert(0, temp)
            i += 1

import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums[:]
        self.origin = nums[:]
        self.len = len(self.origin)

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        i = 0
        while i < self.len:
            j = random.randint(i, self.len - 1)
            temp = self.array[i]
            self.array[i] = self.array[j]
            self.array[j] = temp
            i += 1
        return self.array

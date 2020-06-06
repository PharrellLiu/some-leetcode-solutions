import random
from typing import List


# Shuffle an Array
class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.array = nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        # Fisher-Yates Algorithm
        i = 0
        while i < len(self.array):
            j = random.randint(i, len(self.array) - 1)
            temp = self.array[i]
            self.array[i] = self.array[j]
            self.array[j] = temp
            i += 1
        return self.array


# Min Stack
class MinStack:

    def __init__(self):
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> None:
        self.nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return min(self.nums)

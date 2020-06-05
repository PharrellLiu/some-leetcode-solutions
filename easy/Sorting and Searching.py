from typing import List


# Merge Sorted Array
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = 0
    while i < len(nums1):
        if i >= m:
            nums1[i] = nums2[i - m]
        i += 1
    nums1.sort()


# First Bad Version
def firstBadVersion(self, n):
    
    # The isBadVersion API is already defined for you.
    def isBadVersion(version):
        pass

    left = 1
    right = n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left

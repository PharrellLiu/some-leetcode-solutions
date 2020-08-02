from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        def sort(l, r):
            if l >= r:
                return
            i = l
            j = r
            while i < j:
                while i < j and nums1[j] > nums1[l]:
                    j -= 1
                while i < j and nums1[i] <= nums1[l]:
                    i += 1
                temp = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = temp
            temp = nums1[l]
            nums1[l] = nums1[i]
            nums1[i] = temp
            sort(i + 1, r)
            sort(l, i - 1)

        i = m
        j = 0
        while i < m + n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
        sort(0, m + n - 1)

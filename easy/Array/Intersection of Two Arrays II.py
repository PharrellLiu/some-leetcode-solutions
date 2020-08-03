from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        i = 0
        len_nums = len(nums1)
        while i < len_nums:
            if nums1[i] not in dic:
                dic[nums1[i]] = 1
            else:
                dic[nums1[i]] += 1
            i += 1
        result = []
        len_nums = len(nums2)
        i = 0
        while i < len_nums:
            if nums2[i] in dic and dic[nums2[i]] > 0:
                result.append(nums2[i])
                dic[nums2[i]] -= 1
            i += 1
        return result

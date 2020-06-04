from typing import List


# Remove Duplicates from Sorted Array
def removeDuplicates(self, nums: List[int]) -> int:
    i = 1
    while i < len(nums):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


# Best Time to Buy and Sell Stock II
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    hold = 0
    buyingPrice = 0
    i = 1
    while i < len(prices):
        if prices[i] < prices[i - 1] and hold == 1:
            hold = 0
            profit += prices[i - 1] - buyingPrice
            buyingPrice = 0
        elif prices[i] > prices[i - 1] and hold == 0:
            hold = 1
            buyingPrice = prices[i - 1]
        i += 1
    if hold == 1:
        profit += prices[-1] - buyingPrice
    return profit


# Rotate Array
def rotate(self, nums: List[int], k: int) -> None:
    i = 0
    while i < k:
        temp = nums.pop()
        nums.insert(0, temp)
        i += 1


# Contains Duplicate
def containsDuplicate(self, nums: List[int]) -> bool:
    # or we can use dict/hash table
    return len(nums) != len(set(nums))


# Single Number
def singleNumber(self, nums: List[int]) -> int:
    ans = nums[0]
    i = 1
    while i < len(nums):
        # since x^x=0
        ans ^= nums[i]
        i += 1
    return ans


# Intersection of Two Arrays II
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    ans = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            ans.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
    return ans


# Plus One
def plusOne(self, digits: List[int]) -> List[int]:
    i = len(digits) - 1
    carry = 1
    while i > -1 and carry == 1:
        if digits[i] == 9:
            digits[i] = 0
            carry = 1
        else:
            digits[i] += 1
            carry = 0
        i -= 1
    if carry == 1:
        digits.insert(0, 1)
    return digits


# Move Zeroes
def moveZeroes(self, nums: List[int]) -> None:
    i = 0
    noZero = 0
    while i < len(nums):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[noZero]
            nums[noZero] = temp
            noZero += 1
        i += 1

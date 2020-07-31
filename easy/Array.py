from typing import List


# Remove Duplicates from Sorted Array
def removeDuplicates(self, nums: List[int]) -> int:
    i = 1
    length = len(nums)
    while i < length:
        if nums[i] == nums[i - 1]:
            nums.pop(i)
            length -= 1
        else:
            i += 1
    return length


# Best Time to Buy and Sell Stock II
def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    hold = 0
    buyingPrice = 0
    i = 1
    length = len(prices)
    while i < length:
        if prices[i] < prices[i - 1] and hold == 1:
            hold = 0
            profit += prices[i - 1] - buyingPrice
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
    length = len(nums)
    while i < length:
        # since x^x=0
        ans ^= nums[i]
        i += 1
    return ans


# Intersection of Two Arrays II
def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    dic1 = {}
    i = 0
    len_nums = len(nums1)
    while i < len_nums:
        if nums1[i] not in dic1:
            dic1[nums1[i]] = 1
        else:
            dic1[nums1[i]] += 1
        i += 1
    ans = []
    len_nums = len(nums2)
    i = 0
    while i < len_nums:
        if nums2[i] in dic1 and dic1[nums2[i]] > 0:
            ans.append(nums2[i])
            dic1[nums2[i]] -= 1
        i += 1
    return ans


# Plus One
def plusOne(self, digits: List[int]) -> List[int]:
    i = len(digits) - 1
    carry = 1
    while i > -1 and carry == 1:
        if digits[i] == 9:
            digits[i] = 0
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
    length = len(nums)
    while i < length:
        if nums[i] != 0:
            if i == noZero:
                noZero += 1
            else:
                temp = nums[i]
                nums[i] = nums[noZero]
                nums[noZero] = temp
                noZero += 1
        i += 1


# Two Sum
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    i = 0
    while nums[i] not in dic:
        dic[target - nums[i]] = i
        i += 1
    return [i, dic[nums[i]]]


# Valid Sudoku
def isValidSudoku(self, board: List[List[str]]) -> bool:
    dicForRow = {}
    dicForCol = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}}
    dicForSq = {0: {}, 1: {}, 2: {}}
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            if board[i][j] != ".":
                if board[i][j] in dicForRow:
                    return False
                else:
                    dicForRow[board[i][j]] = 1
                if board[i][j] in dicForCol[j]:
                    return False
                else:
                    dicForCol[j][board[i][j]] = 1
                if board[i][j] in dicForSq[j // 3]:
                    return False
                else:
                    dicForSq[j // 3][board[i][j]] = 1
            j += 1
        dicForRow.clear()
        i += 1
        if i == 3 or i == 6:
            dicForSq.clear()
            dicForSq = {0: {}, 1: {}, 2: {}}
    return True


# Rotate Image
def rotate(self, matrix: List[List[int]]) -> None:
    n = len(matrix) - 1
    i = 0
    while i < (n + 1) // 2:
        j = i
        while j < n - i:
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j][i]
            matrix[n - j][i] = matrix[n - i][n - j]
            matrix[n - i][n - j] = matrix[j][n - i]
            matrix[j][n - i] = temp
            j += 1
        i += 1
# met in the interview of Huawei

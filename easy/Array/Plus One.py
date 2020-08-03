from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        carry = 1
        while i > -1:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] += 1
                carry = 0
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits

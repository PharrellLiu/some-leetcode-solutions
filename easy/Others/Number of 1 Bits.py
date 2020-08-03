class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        count = 0
        for i in n:
            if i == '1':
                count += 1
        return count

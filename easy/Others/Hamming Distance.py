class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        z = bin(z)[2:]
        result = 0
        for i in z:
            if i == '1':
                result += 1
        return result

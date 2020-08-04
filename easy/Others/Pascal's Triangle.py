from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        if numRows == 1:
            return result
        result.append([1, 1])
        if numRows == 2:
            return result
        i = 3
        while i <= numRows:
            curr = [1 for _ in range(i)]
            prev = result[-1]
            j = 1
            while j < i - 1:
                curr[j] = prev[j] + prev[j - 1]
                j += 1
            result.append(curr)
            i += 1
        return result

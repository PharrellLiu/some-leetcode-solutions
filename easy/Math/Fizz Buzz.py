from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        i = 1
        while i <= n:
            s = ''
            if i % 3 == 0:
                s += 'Fizz'
            if i % 5 == 0:
                s += 'Buzz'
            if s == '':
                s = str(i)
            result.append(s)
            i += 1
        return result

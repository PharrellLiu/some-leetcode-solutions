class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True for _ in range(n)]
        i = 2
        count = 0
        while i < n:
            if primes[i] is True:
                count += 1
                j = i + i
                while j < n:
                    primes[j] = False
                    j += i
            i += 1
        return count

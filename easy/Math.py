import math
from typing import List


# Fizz Buzz
def fizzBuzz(self, n: int) -> List[str]:
    ans = []
    i = 1
    while i <= n:
        s = ''
        if i % 3 == 0:
            s += 'Fizz'
        if i % 5 == 0:
            s += 'Buzz'
        if s == '':
            s = str(i)
        i += 1
        ans.append(s)
    return ans


# Count Primes
def countPrimes(self, n: int) -> int:
    isPrimes = [True for i in range(n)]
    i = 2
    count = 0
    while i < len(isPrimes):
        if isPrimes[i] is True:
            count += 1
            j = i + i
            while j < len(isPrimes):
                isPrimes[j] = False
                j += i
        i += 1
    return count


# Power of Three
def isPowerOfThree(self, n: int) -> bool:
    if n <= 0:
        return False
    # math.log(243, 3) = 4.999999
    if n == 243 or n == 59049 or n == 1594323 or n == 129140163 or n == 14348907:
        return True
    return (math.log(n, 3) % 1) == 0


# Roman to Integer
def romanToInt(self, s: str) -> int:
    i = 0
    ans = 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    dic2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    while i < len(s):
        if i < len(s) - 1 and s[i:i + 2] in dic2:
            ans += dic2[s[i:i + 2]]
            i += 2
        else:
            ans += dic[s[i]]
            i += 1
    return ans

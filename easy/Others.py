# Number of 1 Bits
def hammingWeight(self, n: int) -> int:
    s = bin(n)
    count = 0
    i = 2
    while i < len(s):
        if s[i] == '1':
            count += 1
        i += 1
    return count


# Hamming Distance
def hammingDistance(self, x: int, y: int) -> int:
    z = x ^ y
    z = bin(z)[2:]
    ans = 0
    for i in z:
        if i == '1':
            ans += 1
    return ans


# Reverse Bits
def reverseBits(self, n: int) -> int:
    n = "{:032b}".format(n)
    return int(n[::-1], 2)



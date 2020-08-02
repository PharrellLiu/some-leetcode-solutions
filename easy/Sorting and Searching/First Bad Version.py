def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        l = 0
        r = n
        while l < r:
            mid = l + (r - l) // 2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
        return l

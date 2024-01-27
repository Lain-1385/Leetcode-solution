# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadversion(mid) == False:
                right = mid - 1
            else:
                left = mid + 1
            return mid


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        left = 1
        right = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid) == True:
                right = mid - 1
            else:
                left = mid + 1
        return left 
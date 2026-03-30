'''https://leetcode.com/problems/first-bad-version/'''


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        if n == 1 and isBadVersion(n):
            return n
        while right >= left:
            mid = (left + right) // 2
            tf_mid = isBadVersion(mid)
            tf_right = isBadVersion(mid + 1)

            if not tf_mid and tf_right:
                return mid + 1
            elif tf_mid and tf_right:
                right = mid - 1
            else:
                left = mid + 1
            print(tf_mid, tf_right, mid)
        return 1

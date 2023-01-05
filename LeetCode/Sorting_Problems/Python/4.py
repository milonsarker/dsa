#https://leetcode.com/problems/median-of-two-sorted-arrays/description/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        lngth  = len(nums1)
        if lngth % 2 == 1:
            return nums1[lngth//2]
        else:
            return (nums1[lngth//2 -1] + nums1[lngth//2])/2
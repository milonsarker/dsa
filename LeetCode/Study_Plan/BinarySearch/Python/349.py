'''https://leetcode.com/problems/intersection-of-two-arrays/'''

'''
Notes: Not sure why this problem classified as Binary Search. 
Its more like a hashing problem. 
'''

'''One Liner'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))

'''Using Hashing'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f_hash = {}
        for num in nums1:
            if num in f_hash:
                f_hash[num] += 1
            else:
                f_hash[num] = 1
        result = []
        for num in nums2:
            if num in f_hash and num not in result:
                result.append(num)
        return result
#https://leetcode.com/problems/contains-duplicate/

#__Simple Solution Using set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pre_l = len(nums)
        set_l = len(set(nums))
        if pre_l > set_l:
            return True
        else:
            return False

#__Hashing Method
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        item_count = {}
        for i in nums:
            if i in item_count:
                return True
            else:
                item_count[i] = 1
        return False
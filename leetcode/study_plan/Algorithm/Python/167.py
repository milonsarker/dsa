'''https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/'''

'''Hashing Algorithm: Complexity: O(n)'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(numbers)):
            gap = target - numbers[i]
            if numbers[i] in hash_map:
                return [hash_map[numbers[i]]+1,i+1]
            else:
                hash_map[gap] = i

'''Algorithm: Two Pointers; Time Complexity : O(n)'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while right > left:
            summ = numbers[left] + numbers[right]
            if target == summ:
                return [left + 1, right + 1]
            elif summ > target:
                right -= 1
            else:
                left += 1
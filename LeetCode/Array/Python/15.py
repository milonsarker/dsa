#https://leetcode.com/problems/3sum/description/

#Brute-Force Solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        leng = len(nums)
        result = []
        for i in range(leng):
            for j in range(i + 1, leng):
                for k in range(j + 1, leng):
                    if nums[i] + nums[j] + nums[k] == 0:
                        lst = []
                        lst = [nums[i], nums[j], nums[k]]
                        lst.sort()
                        if lst not in result:
                            result.append(lst)
        #print(set(result))
        return result

# Optimized Solution

class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        result = []
        while right > left:
            summ = numbers[left] + numbers[right]
            if target == summ:
                if [left, right] not in result:
                    result.append([numbers[left], numbers[right]])
                left += 1
                right -= 1
            elif summ > target:
                right -= 1
            else:
                left += 1
        if len(result) > 0:
            return result
        else:
            return None

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        leng = len(nums)
        nums.sort()
        result = []
        previous_ele = None
        for i in range(leng - 2):
            if previous_ele == nums[i]:
                continue
            else:
                previous_ele = nums[i]
            target = nums[i] * (-1)
            ret_val = self.twoSum(nums[i+1:], target)
            if ret_val == None:
                continue
            for x in ret_val:
                triplet = [nums[i],x[0], x[1]]
                if triplet not in result:
                    result.append(triplet)
        return result
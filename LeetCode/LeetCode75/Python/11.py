#https://leetcode.com/problems/container-with-most-water/

#Brute_Force Solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        leng = len(height)
        for i in range(leng):
            for j in range(i+1, leng):
                max_water = max((j - i) * min(height[i], height[j]), max_water)
        return max_water

#Complexity : O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        leng = len(height)
        left, right = 0, leng - 1
        while right > left:
                max_water = max((right - left) * min(height[left], height[right]), max_water)
                if height[left] > height[right]:
                    right -= 1
                else:
                    left += 1
        return max_water
#https://leetcode.com/problems/maximum-sum-circular-subarray/description/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        arrSum = nums[0]
        aiSum, aiMaxSum = nums[0], nums[0]
        nSum, nMaxSum = -nums[0], -nums[0]
        for i in nums[1:]:
            arrSum += i

            #Positive part
            aiSum = max(i, aiSum + i)
            aiMaxSum = max(aiMaxSum, aiSum)

            #Negative part
            temp_val = - i
            nSum = max(temp_val, nSum + temp_val)
            nMaxSum = max(nMaxSum, nSum)

        cirSum = arrSum + nMaxSum

        print(arrSum, cirSum, aiMaxSum, nMaxSum)
        if cirSum > aiMaxSum and cirSum != 0:
            return cirSum
        else:
            return aiMaxSum
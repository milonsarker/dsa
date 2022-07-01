//https://leetcode.com/problems/maximum-subarray/

//Kadane's Algorithm

class Solution
{
    public:
        int maxSubArray(vector<int>& nums)
        {
            int curr_subarr =  nums[0];
            int max_subarr = nums[0];
            for ( int i = 1; i < nums.size(); i++ )
            {
                curr_subarr = max( nums[i], curr_subarr + nums[i] );
                max_subarr = max( curr_subarr, max_subarr );
            }
            return max_subarr;
        }
};
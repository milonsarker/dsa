//https://leetcode.com/problems/two-sum/

class Solution
{
    public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        int diff;
        unordered_map<int,int> hash_map;
        for ( int i = 0; i < nums.size(); i++ )
        {
            diff = target - nums[i];
            if ( hash_map.find(nums[i]) == hash_map.end() )
            {
                hash_map[diff] = i;
            }
            else
            {
                return {hash_map[nums[i]], i};
            }
        }
        return {-1,-1};
    }
};
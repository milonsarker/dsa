//https://leetcode.com/problems/contains-duplicate/

class Solution
{
    public:
        bool containsDuplicate(vector<int>& nums)
        {
            unordered_map<int, int> hash_map;
            for (int i = 0; i < nums.size(); i++)
            {
                if( hash_map.find(nums[i]) == hash_map.end() )
                {
                    hash_map[nums[i]] = 1;
                }
                else
                {
                    return true;
                }
            }
            return false;

        }
};
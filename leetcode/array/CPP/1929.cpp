//https://leetcode.com/problems/concatenation-of-array/description/


class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums)
    {
        vector <int> ans;
        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            nums.push_back(nums[i]);
        }
        return nums;
    }
};
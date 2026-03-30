//https://leetcode.com/problems/intersection-of-two-arrays-ii/

//Hashing
class Solution
{
    public:
        vector<int> intersect(vector<int>& nums1, vector<int>& nums2)
        {
            unordered_map <int, int> hash_map;
            vector <int> result;
            for(int i = 0; i < nums1.size(); i++)
            {
                if ( hash_map.find(nums1[i]) == hash_map.end())
                {
                    hash_map[nums1[i]] = 1;
                }
                else
                {
                    hash_map[nums1[i]] += 1;
                }
            }
            for (int i = 0; i < nums2.size(); i++ )
            {
                if (hash_map.find(nums2[i]) == hash_map.end())
                {
                    continue;
                }
                else
                {
                    if (hash_map[nums2[i]] > 0)
                    {
                        result.push_back(nums2[i]);
                        hash_map[nums2[i]] -= 1;
                    }
                }
            }
            return result;
        }
};
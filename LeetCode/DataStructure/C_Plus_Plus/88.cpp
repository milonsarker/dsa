//https://leetcode.com/problems/merge-sorted-array/

//Three Pointers (Start From the Beginning)
class Solution
{
    public:
        void merge(vector<int>& nums1, int m, vector<int>& nums2, int n)
        {
            int nums1copy[m+n];
            for (int i = 0; i < m; i++ )
            {
                nums1copy[i] = nums1[i];
            }
            int p1 = 0;
            int p2 = 0;
            for ( int i = 0; i < (m + n); i++)
            {
                if ( p2 >=n or (p1 < m and nums1copy[p1] <= nums2[p2]) )
                {
                    nums1[i] = nums1copy[p1];
                    p1++;
                }
                else
                {
                    nums1[i] = nums2[p2];
                    p2++;
                }
            }
        }
};
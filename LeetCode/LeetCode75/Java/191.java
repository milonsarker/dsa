//https://leetcode.com/problems/number-of-1-bits/description/

//Simple Solution

public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n)
    {
        int bits = 0;
        int mask = 1;
        for( int i = 0; i < 32; i ++)
        {
            if ((mask & n) != 0)
            {
                bits++;
            }
            mask = mask << 1;
        }
        return bits;
    }
}

//Optimal Solution
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n)
    {
        int bits = 0;
        while (n != 0)
        {
            bits++;
            n = n & (n - 1);
        }
        return bits;
    }
}
#https://leetcode.com/problems/sum-of-two-integers/description/
//Using XOR and AND and left shift bitwise operator
class Solution {
    public int getSum(int a, int b) {
        while (b != 0){
            int temp;
            temp = (a & b) << 1;
            a = (a ^ b);
            b = temp;
        }
        return a;
    }
}
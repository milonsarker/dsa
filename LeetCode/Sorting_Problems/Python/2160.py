'''https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/'''


'''Solution: Out of my head. Used built-in sort function'''
class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = list(str(num))
        num_list = list(map(int, num_list))
        num_list.sort()

        new1 = int(str(num_list[0]) + str(num_list[2]))
        new2 = int(str(num_list[1]) + str(num_list[3]))
        return new1 + new2
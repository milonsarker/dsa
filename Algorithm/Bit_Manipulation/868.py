#https://leetcode.com/problems/binary-gap/description/


class Solution:
    def binaryGap(self, n: int) -> int:
        binary_num = bin(n)[2:]
        max_gap = 0
        start = 0
        cnt = 1
        for i in binary_num:
            if start == 0 and i == '1':
                start = 1
            elif start == 1 and i == '1':
                start = 1
                if max_gap < cnt:
                    max_gap = cnt
                cnt = 1
            if start == 1 and i == '0':
                cnt += 1
        return max_gap

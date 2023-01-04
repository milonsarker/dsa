#https://leetcode.com/problems/longest-palindrome/description/


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_cnt = {}

        for i in s:
            if i in char_cnt:
                char_cnt[i] += 1
            else:
                char_cnt[i] = 1
        lngth = 0
        cnt_one_flag = False
        flag = False
        for key, val in char_cnt.items():
            if val % 2 == 0:
                lngth += val
            elif val > 2 and val % 2 != 0:
                lngth += val - 1
                flag = True
            elif val == 1:
                cnt_one_flag = True
        return lngth + 1 if cnt_one_flag or flag else lngth
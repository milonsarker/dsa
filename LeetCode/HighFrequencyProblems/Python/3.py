#https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = {}
        max_cntr = 0
        cntr = 0
        for i in range(len(s)):
            if s[i] not in hmap:
                hmap[s[i]] = i+1
                cntr += 1
                if cntr > max_cntr:
                    max_cntr = cntr
            else:
                cntr = i + 1 - hmap[s[i]]
                pntr_val = hmap[s[i]]
                hmap = {key:val for key, val in hmap.items() if val > pntr_val}
                hmap[s[i]] = i+1
        return max_cntr
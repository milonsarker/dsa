#https://leetcode.com/problems/flip-string-to-monotone-increasing/description/


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cnt = { '1' : 0, '0': 0}
        for i in s:
            cnt[i] += 1
        ans = cnt['0']
        m = cnt['0']
        for i in s:
            if i == '0':
                m -= 1
                ans = min(ans, m)
            else:
                m +=1
        print(cnt)
        return ans
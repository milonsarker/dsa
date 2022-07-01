'''https://leetcode.com/problems/isomorphic-strings/'''

''''''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}
        for i, j in zip(s, t):
            if i not in map_st and j not in map_ts:
                map_st[i] = j
                map_ts[j] = i

            elif map_st.get(i) != j or map_ts.get(j) != i:
                return False
        return True

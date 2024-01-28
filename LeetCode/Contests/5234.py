#--https://leetcode.com/contest/weekly-contest-293/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        found ={}
        word_n = ''
        for i in range(len(words)):
            word = ''.join(sorted(words[i]))
            if i == 0:
                result.append(words[i])
            elif word == word_n:
                continue
            else:
                result.append(words[i])
            word_n = word
        return result
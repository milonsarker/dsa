#https://leetcode.com/problems/concatenated-words/description/

#Learn

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        visited_indices: set[int] = set()
        words_set: set[str] = set(words)
        def dfs_other_words(word: str, start_idx: int):
            n = len(word)
            if start_idx == n:
                # Got past the end - the word is made of multiple words.
                return True
            if start_idx in visited_indices:
                # We already searched from this index.
                return False
            
            visited_indices.add(start_idx)
            # Go up til the last character in the word if we are starting
            # from the first index. Otherwise we'll mark single words as results.
            for i in range(start_idx + 1, (n + 1 if start_idx != 0 else n)):
                if (word[start_idx:i] in words_set
                    and dfs_other_words(word, i)):
                    return True
            
            return False

        result: list[str] = []
        for word in words:
            visited_indices.clear()
            if dfs_other_words(word, 0):
                result.append(word)
        
        return result

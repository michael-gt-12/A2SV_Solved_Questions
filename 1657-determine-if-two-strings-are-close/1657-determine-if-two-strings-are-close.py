class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter

        word1_freq = Counter(word1)
        word2_freq = Counter(word2)

        if len(word1) == len(word2):
            if set(word1) == set(word2):
                if sorted(list(word1_freq.values())) == sorted(list(word2_freq.values())):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
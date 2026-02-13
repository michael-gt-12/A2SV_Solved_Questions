class Solution:
    def findValidPair(self, s: str) -> str:
        from collections import Counter
        s_freq_map = Counter(s)
        left = 0
        right = 1
        while right < len(s):
            if s[left] != s[right]:
                if s_freq_map[s[left]] == int(s[left]) and s_freq_map[s[right]] == int(s[right]):
                    return s[left:right+1]
            left += 1
            right += 1
        return ""

        
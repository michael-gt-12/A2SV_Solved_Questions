class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result = []
        my_dict = {}
        for i in range(len(s)):
            my_dict[s[i]] = i
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end,my_dict[s[i]])
            if i == end:
                result.append(end-start+1)
                start = i+1
        return result

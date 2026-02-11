class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        index_map = {}
        for i in range(len(s)):
            index_map[i] = indices[i]
        result = [0]*len(s)
        for item in index_map.items():
            result[item[1]] = s[item[0]]
        result = "".join(result)
        return result

        
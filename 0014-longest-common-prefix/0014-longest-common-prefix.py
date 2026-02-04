class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        word = strs[0]
        for i in range(len(word)):
            for j in range(len(strs)):
                if i < len(strs[j]):
                    if word[i] != strs[j][i]:
                        return "".join(result)
                else:
                    return "".join(result)
            result.append(word[i])
        return "".join(result)

        
            


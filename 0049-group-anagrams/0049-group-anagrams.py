from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        seen=[]
        for i in range(len(strs)):
            if strs[i] in seen:
                    continue
            current = [strs[i]]
            word_dict = Counter(strs[i])
            for j in range(i+1,len(strs)):
                if strs[j] in seen:
                    continue
                word_j_dict = Counter(strs[j])
                if word_dict == word_j_dict:
                    current.append(strs[j])
                    seen.append(strs[j])
            answer.append(current)
        return answer




        
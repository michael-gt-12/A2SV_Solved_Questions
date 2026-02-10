from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}
        for i in strs:
            temp = str(sorted(i))
            if temp in anagram:
                anagram[temp].append(i)
            else:
                anagram[temp] = [i]
        answer = []
        for value in anagram.values():
            answer.append(value)
        return answer

       
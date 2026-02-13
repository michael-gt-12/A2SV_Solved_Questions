class Solution:
    def frequencySort(self, s: str) -> str:
        smap = Counter(s)
        return "".join(char * freq for char , freq in smap.most_common())

        

        
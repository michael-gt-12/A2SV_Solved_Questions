from collections import defaultdict

class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        a_dict = defaultdict()
        b_dict = defaultdict()
        for i in range(len(a)):
            if a[i] in a_dict.keys():
                a_dict[a[i]] += 1
            else:
                a_dict[a[i]] = 1
            if b[i] in b_dict.keys():
                b_dict[b[i]] += 1
            else:
                b_dict[b[i]] = 1
        if a_dict == b_dict:
            return True
        else:
            return False

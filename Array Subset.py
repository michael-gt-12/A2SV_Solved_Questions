#User function Template for python3
from collections import defaultdict
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a_dict = defaultdict()
        b_dict = defaultdict()
        for i in range(len(a)):
            if a[i] in a_dict.keys():
                a_dict[a[i]] += 1
            else:
                a_dict[a[i]] = 1
        for i in range(len(b)):
            if b[i] in b_dict.keys():
                b_dict[b[i]] += 1
            else:
                b_dict[b[i]] = 1
        
        for b in b_dict.keys():
            if b not in a_dict.keys():
                return False
            else:
                if b_dict[b] > a_dict[b]:
                    return False
                
                
        return True

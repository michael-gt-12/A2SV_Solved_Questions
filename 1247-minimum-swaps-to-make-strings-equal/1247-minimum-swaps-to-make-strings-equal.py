# class Solution:
#     def minimumSwap(self, s1: str, s2: str) -> int:
#         from collections import Counter

#         s1_freq = {"x":s1.count("x"),"y":s1.count("y")}
#         s2_freq = {"x":s2.count("x"),"y":s2.count("y")}

#         if s1 == s2:
#             return 0
#         else:
#             if sorted(s1_freq.values()) == sorted(s2_freq.values()):
#                 return max(s1_freq.values())
#             else:
#                 return -1

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
        
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
        
        if (xy + yx) % 2 != 0:
            return -1
        
        return (xy // 2) + (yx // 2) + (2 if xy % 2 else 0)
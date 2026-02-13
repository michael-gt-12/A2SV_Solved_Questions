class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        rans_map = Counter(ransomNote)
        mag_map = Counter(magazine)

        flag = False

        if mag_map == rans_map:
            return True
        else:
            for key in rans_map:
                if mag_map[key] < rans_map[key] or key not in mag_map:
                    return False
            else:
                return True
                    
            # else:
            #     return True
        
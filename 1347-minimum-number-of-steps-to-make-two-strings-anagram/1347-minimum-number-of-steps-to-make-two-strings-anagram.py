class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        count = 0
        s_counter = Counter(s)
        t_counter = Counter(t)
        if s_counter == t_counter:
            return 0 
        else:
            for key in s_counter:
                if key not in t_counter:
                    count += s_counter[key]
                else:
                    if s_counter[key] > t_counter[key]:
                        count += s_counter[key] - t_counter[key]
        return count


        
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        prefix = [0] * n
        for shift in shifts:
            if shift[2] == 1:
                prefix[shift[0]] += 1
                if shift[1] + 1 < n:
                    prefix[shift[1]+1] -= 1
            else:
                prefix[shift[0]] -= 1
                if shift[1] + 1 < n:
                    prefix[shift[1]+1] += 1
        
        prefix_sum = []
        total = 0
        for num in prefix:
            total += num
            prefix_sum.append(total)

        result = []
        for i in range(n):
            shift = prefix_sum[i]
            char_val = ord(s[i]) - ord("a")
            new_char_val = (char_val + shift) % 26
            new_char = chr(new_char_val + ord("a"))
            result.append(new_char)
            
        return "".join(result)

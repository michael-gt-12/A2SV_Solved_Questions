class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_ind , _ = stack.pop()
                answer[prev_ind] = i - prev_ind
            stack.append((i,temp))

        return answer

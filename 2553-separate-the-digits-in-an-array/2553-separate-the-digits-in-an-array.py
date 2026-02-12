class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            num = str(num)  
            for char in num:
                answer.append(int(char))  
        return answer
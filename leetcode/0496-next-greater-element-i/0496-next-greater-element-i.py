class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        num_map = {}
        stack = []

        for num in nums2:
            while stack and  stack[-1] < num:
                num_map[stack.pop()] = num

            stack.append(num)
        
        for num in nums2:
            if num not in num_map:
                num_map[num] = -1

        answer = []

        for num in nums1:
            answer.append(num_map[num])
        return answer

        

     
                


        
            

        
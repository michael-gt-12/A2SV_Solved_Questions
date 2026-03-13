class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_stack = []
        current_min = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1]:
                stack.pop()
                min_stack.pop()

            if stack and n > min_stack[-1]:
                return True

            stack.append(n)
            min_stack.append(current_min)

            current_min = min(current_min,n)
        return False
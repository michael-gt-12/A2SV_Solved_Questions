class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        queue = deque()

        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        answer.append(queue[0])

        left = 0
        for i in range(k,len(nums)):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            if nums[left] == queue[0]:
                queue.popleft()
            left += 1
            answer.append(queue[0])
        return answer


            

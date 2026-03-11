class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        mon_inc = deque()
        mon_dec = deque()
        left = 0
        count = 0

        for r in range(len(nums)):
            while mon_inc and mon_inc[-1] > nums[r]:
                mon_inc.pop()
            mon_inc.append(nums[r])

            while mon_dec and mon_dec[-1] < nums[r]:
                mon_dec.pop()
            mon_dec.append(nums[r])

            while mon_dec and mon_inc and not mon_dec[0] - mon_inc[0] <= limit:
                if mon_dec[0] == nums[left]:
                    mon_dec.popleft()
                if mon_inc[0] == nums[left]:
                    mon_inc.popleft()
                left += 1
            
            count = max(count , r - left + 1)
        return count
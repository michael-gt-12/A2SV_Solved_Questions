class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        triangle = nums[:3]
        check_sum = sum(nums[:2])
        check = nums[2]
        max_par = 0
        left = 0
        right = 2
        while right < len(nums):
            if check_sum > check:
                max_par = max(max_par,check_sum + check)
            check_sum -= nums[left]
            left += 1
            check_sum += nums[right]
            right += 1
            if right < len(nums):
                check = nums[right]
        return max_par

        
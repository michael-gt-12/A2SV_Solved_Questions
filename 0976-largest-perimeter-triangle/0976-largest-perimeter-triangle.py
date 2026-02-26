class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        Sum = 0
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        else:
            return 0

        # check_sum = sum(nums[:2])
        # check = nums[2]
        # max_par = 0
        # left = 0
        # right = 2
        # while right < len(nums):
        #     if check_sum > check:
        #         max_par = max(max_par,check_sum + check)
        #     check_sum -= nums[left]
        #     left += 1
        #     check_sum += nums[right]
        #     right += 1
        #     if right < len(nums):
        #         check = nums[right]
        # return max_par

        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1
            else:
                result = mid
                break

        if result == -1:
            return bisect_right(nums,target)
        else:
            return bisect_left(nums,target)
        
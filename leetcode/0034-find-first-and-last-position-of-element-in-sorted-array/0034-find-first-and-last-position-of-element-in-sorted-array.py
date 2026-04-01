class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low = 0
        high = len(nums) - 1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if index == -1:
            return [-1,-1]
        else:
            left = bisect_left(nums,target)
            right = bisect_right(nums,target)
            return [left , right-1]

            # i = index
            # while i < len(nums):
            #     if nums[index] == nums[i]:
            #         i += 1
            #     else:
            #         break

            # j = index
            # while j > -1:
            #     if nums[index] == nums[j]:
            #         j -= 1
            #     else:
            #         break

            # return [j+1,i-1]





        
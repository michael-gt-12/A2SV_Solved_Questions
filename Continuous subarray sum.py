class Solution:
    def checkSubarraySum(self, nums, k):
        mod_index = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            prefix %= k

            if prefix in mod_index:
                if i - mod_index[prefix] >= 2:
                    return True
            else:
                mod_index[prefix] = i

        return False

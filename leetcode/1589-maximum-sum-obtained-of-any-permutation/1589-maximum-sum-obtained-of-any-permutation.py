class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n)

        for request in requests:
            l , r = request
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1

        for i in range(1, n):
            freq[i] += freq[i - 1]

        nums.sort()
        freq.sort()

        result = 0
        for i in range(n):
            result = (result + nums[i] * freq[i]) % (10**9 + 7)

        return result
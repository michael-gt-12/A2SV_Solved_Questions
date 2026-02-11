class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_map = {}

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_map[i] = nums[i]

        sum_even = sum(even_map.values())
        answer = []

        for query in queries:
            val, idx = query

            if idx in even_map:
                sum_even -= even_map[idx]
                nums[idx] += val

                if nums[idx] % 2 == 0:
                    even_map[idx] = nums[idx]
                    sum_even += nums[idx]
                else:
                    del even_map[idx]

            else:
                nums[idx] += val

                if nums[idx] % 2 == 0:
                    even_map[idx] = nums[idx]
                    sum_even += nums[idx]

            answer.append(sum_even)

        return answer

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        left = 0
        right = 1
        count = 1
        cur = points[left][1]

        while right < len(points):
            if points[right][0] > cur:
                count += 1
                cur = points[right][1]
                left = right
            right += 1

        return count
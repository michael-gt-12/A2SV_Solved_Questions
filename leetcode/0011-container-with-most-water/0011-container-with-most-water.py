class Solution:
    def maxArea(self, height: List[int]) -> int:
        n =len(height)
        a = 0
        b = n-1
        area = min([height[a],height[b]]) * (b - a)
        while a <= b:
            if area >= min([height[a],height[b]]) * (b - a):
                if height[a] <= height[b]:
                    a += 1
                else:
                    b -= 1
            else:
                area = min([height[a],height[b]]) * (b - a)
                if height[a] <= height[b]:
                    a += 1
                else:
                    b -= 1
        return area

            

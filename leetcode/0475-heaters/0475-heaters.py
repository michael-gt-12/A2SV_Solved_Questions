class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # result = []

        # for house in houses:
        #     distances = []
        #     for heater in heaters:
        #         distances.append(abs(house - heater))

        #     result.append(min(distances))

        # return max(result)
            
        # uncovered = set(houses) - set(heaters)
        # ranges = [[heater,heater] for heater in heaters]
        # radius = 0
        # while uncovered:
        #     radius += 1
        #     for rng in ranges:
        #         rng[0] -= 1
        #         rng[1] += 1
        #         uncovered.discard(rng[0])
        #         uncovered.discard(rng[1])
        # return radius
        
        # radius = 0
        # for house in houses:
        #     min_dist = float("inf")
        #     for heater in heaters:
        #         min_dist = min(min_dist, abs(heater-house))
        #     radius = max(radius,min_dist)
        # return radius

        def dist_closest(heaters,house):
            left , right = 0 , len(heaters) - 1
            min_dist = float("inf")
            while left <= right:
                mid = (left + right) // 2
                min_dist = min(min_dist,abs(heaters[mid] - house))
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return min_dist
        
        heaters.sort()
        radius = 0
        for house in houses:
            radius = max(radius,dist_closest(heaters,house))
        return radius
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        myPile = 0
        l = 0
        right = len(piles) 
        while l < right:
            myPile += piles[right-2]
            right = right - 2
            l += 1
        return myPile

        
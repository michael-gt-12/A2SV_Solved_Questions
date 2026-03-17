class Solution:
    def myPow(self, x: float, n: int) -> float:
        # base case
        if n == 0:
            return 1

        # for negative numbers
        if n < 0:
            return 1 / self.myPow(x,-n)

        # recurrence relation

        if n % 2 == 0:
            half = self.myPow(x,n//2)
            return half * half
        else:
            return x * self.myPow(x,n-1)

        
        
        


        
            
        

        
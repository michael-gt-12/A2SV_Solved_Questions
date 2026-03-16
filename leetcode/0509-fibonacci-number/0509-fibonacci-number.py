class Solution:
    def fib(self, n: int) -> int:
        # Base case
        if n == 1:
            return 1
        if n == 0:
            return 0

        # recurrence relation and the state
        return self.fib(n - 1) + self.fib(n - 2)
        
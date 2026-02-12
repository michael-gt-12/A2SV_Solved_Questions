class Solution:
    def isHappy(self, n: int) -> bool:
        checker=set()
        while n != 1 and n not in checker:
            checker.add(n)
            s_n=str(n)
            num=0
            for i in s_n:
                num += int(i) * int(i)
            n = num
        return n == 1

            
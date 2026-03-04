class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        les_num = range(int(sqrt(c))+1)
        n = len(les_num)
        a = 0
        b = n-1
        result = False
        while a <= b:
            if (pow(les_num[a],2) + pow(les_num[b],2) == c):
                result = True
                break
            elif (pow(les_num[a],2) + pow(les_num[b],2) > c):
                b -= 1
            else:
                a += 1
                
        return result
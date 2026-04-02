class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.pref = [[0]*(col+1) for _ in range(row+1)]
        for i in range(row):
            for j in range(col):
                self.pref[i][j] = self.pref[i-1][j] + self.pref[i][j-1] - self.pref[i-1][j-1]+matrix[i][j]

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.pref[row2][col1-1]
        right = self.pref[row1-1][col2]
        dig = self.pref[row1-1][col1-1]
        cur = self.pref[row2][col2]
        return cur-left-right+dig

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
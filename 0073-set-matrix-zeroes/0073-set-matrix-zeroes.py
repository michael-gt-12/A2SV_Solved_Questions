class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeros.append([i,j])
        
        for zero in zeros:
            row = zero[0]
            col = zero[1]
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
            for j in range(len(matrix)):
                matrix[j][col] = 0

        
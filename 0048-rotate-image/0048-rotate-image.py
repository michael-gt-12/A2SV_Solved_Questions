class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(r, cols):
                matrix[c][r] , matrix[r][c] = matrix[r][c] , matrix[c][r]
        
        for row in matrix:
            row.reverse()
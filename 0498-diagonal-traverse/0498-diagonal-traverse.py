class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        result = []
        cur_row = 0
        cur_col = 0
        going_up = True

        while len(result) != rows * cols:
            if going_up:
                while cur_row >= 0 and cur_col < cols:
                    result.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if cur_col == cols:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                going_up = False
            else:
                while cur_row < rows and cur_col >= 0:
                    result.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                if cur_row == rows:
                    cur_col += 2
                    cur_row -= 1
                else:
                    cur_col += 1
                going_up = True
            
        return result


        
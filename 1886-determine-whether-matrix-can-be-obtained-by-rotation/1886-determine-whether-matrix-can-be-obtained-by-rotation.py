class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        rows = len(mat)

        if mat == target:
            return True

        count = 0
        while count < 3:
            check = [[0]*rows for _ in range(rows)]
            for r in range(rows):
                for c in range(rows):
                    check[r][c] = mat[rows - 1 - c][r]

            if check == target:
                return True

            mat = check
            count += 1

        return False
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        import copy
        rows = len(mat)
        cols = len(mat[0])
        check = [[0]*cols for _ in range(rows)]
        count = 0
        while count < 3:
            check = [[0]*cols for _ in range(rows)]
            for r in range(rows):
                for c in range(cols):
                    check[r][c] = mat[rows - 1 - c][r]
            if check == target:
                return True
            mat = copy.deepcopy(check)
            count += 1
        else:
            return False



        
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        Rows = len(img)
        Cols = len(img[0])

        result = [[0]*Cols for _ in range(Rows)]

        for r in range(Rows):
            for c in range(Cols):
                total = 0
                count = 0
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if i < 0 or i == Rows or j < 0 or j == Cols:
                            continue
                        total += img[i][j]
                        count += 1
                result[r][c] = total // count
        return result
                
        
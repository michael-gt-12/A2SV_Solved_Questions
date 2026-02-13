matrix = []
for i in range(5):
    row = list(map(int,input().split()))
    matrix.append(row)
for i in range(5):
    if 1 in matrix[i]:
        row = i+1
        column = matrix[i].index(1)+1
        break
moves = abs(row-3) + abs(column-3)
print(moves)

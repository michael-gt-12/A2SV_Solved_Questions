n, m = map(int, input().split())
grid = [input() for _ in range(n)]

h = [[0]*m for _ in range(n)]
v = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if j+1 < m and grid[i][j] == '.' and grid[i][j+1] == '.':
            h[i][j] = 1
        if i+1 < n and grid[i][j] == '.' and grid[i+1][j] == '.':
            v[i][j] = 1

ph = [[0]*(m+1) for _ in range(n+1)]
pv = [[0]*(m+1) for _ in range(n+1)]

for i in range(n):
    for j in range(m):
        ph[i+1][j+1] = h[i][j] + ph[i][j+1] + ph[i+1][j] - ph[i][j]
        pv[i+1][j+1] = v[i][j] + pv[i][j+1] + pv[i+1][j] - pv[i][j]

def get_sum(pref, r1, c1, r2, c2):
    return pref[r2][c2] - pref[r1][c2] - pref[r2][c1] + pref[r1][c1]

q = int(input())
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1; c1 -= 1

    horizontal = get_sum(ph, r1, c1, r2, c2-1)
    vertical = get_sum(pv, r1, c1, r2-1, c2)

    print(horizontal + vertical)
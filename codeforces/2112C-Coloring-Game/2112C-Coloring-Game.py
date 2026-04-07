import bisect

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    answer = 0
    for i in range(n):
        for j in range(i):
            x = max(a[n - 1], 2 * a[i]) - a[i] - a[j]
            k = bisect.bisect_right(a, x, 0, j)
            answer += j - k
    
    print(answer)
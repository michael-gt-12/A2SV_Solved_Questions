n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == n:
    print(0)
    exit()

L = 0
R = 1
total = 0
gaps = []

while R < n:
    diff = a[R] - a[L]
    total += diff
    gaps.append(diff)
    L += 1
    R += 1

gaps.sort(reverse=True)

answer = total - sum(gaps[:k-1])
print(answer)

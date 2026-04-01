n, k, q = map(int, input().split())

MAX_T = 200000 + 2 

diff = [0] * (MAX_T)

for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

freq = [0] * (MAX_T)
for i in range(1, MAX_T):
    freq[i] = freq[i - 1] + diff[i]

good = [0] * (MAX_T)
for i in range(1, MAX_T):
    if freq[i] >= k:
        good[i] = 1

prefix_good = [0] * (MAX_T)
for i in range(1, MAX_T):
    prefix_good[i] = prefix_good[i - 1] + good[i]

for _ in range(q):
    a, b = map(int, input().split())
    print(prefix_good[b] - prefix_good[a - 1])
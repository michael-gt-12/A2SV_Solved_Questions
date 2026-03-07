t = int(input())
for _ in range(t):
    n = int(input())
    seq = list(map(int,input().split()))

    l = 0
    r = n - 1
    result = []
    while l <= r :
        if l == r:
            result.append(seq[l])
            break

        result.append(seq[l])
        result.append(seq[r])
        l += 1
        r -= 1

    print(*result)
from collections import Counter

t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    socks = list(map(int, input().split()))

    left = Counter(socks[:l])
    right = Counter(socks[l:])

    for color in list(left.keys()):
        m = min(left[color], right.get(color, 0))
        left[color] -= m
        right[color] -= m
        l -= m
        r -= m

    ans = 0

    if l > r:
        left, right = right, left
        l, r = r, l

    diff = (r - l) // 2

    for color in right:
        pairs = right[color] // 2
        use = min(diff, pairs)

        ans += use
        right[color] -= 2 * use
        r -= 2 * use
        diff -= use

        if diff == 0:
            break

    ans += diff
    r -= diff
    l += diff

    ans += (l + r) // 2

    print(ans)
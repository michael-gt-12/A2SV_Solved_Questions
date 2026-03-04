from collections import Counter

T = int(input())
for _ in range(T):
    s = input().strip()
    t = input().strip()

    tt = Counter(t)
    ss = Counter(s)

    if any(tt[c] < ss[c] for c in ss):
        print("Impossible")
        continue

    for c in s:
        tt[c] -= 1

    remaining = []
    for c in tt:
        remaining.extend([c] * tt[c])

    remaining.sort()

    ans = []
    i = j = 0

    while i < len(remaining) and j < len(s):
        if remaining[i] < s[j]:
            ans.append(remaining[i])
            i += 1
        else:
            ans.append(s[j])
            j += 1

    ans.extend(remaining[i:])
    ans.extend(s[j:])

    print("".join(ans))
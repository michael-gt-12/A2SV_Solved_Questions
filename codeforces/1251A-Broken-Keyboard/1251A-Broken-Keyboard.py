t = int(input())
for _ in range(t):
    s = input().strip()
    
    ans = [False] * 26
    n = len(s)
    
    i = 0
    while i < n:
        j = i
        while j + 1 < n and s[j + 1] == s[i]:
            j += 1
        
        if (j - i) % 2 == 0:
            ans[ord(s[i]) - ord('a')] = True
        
        i = j + 1
    
    for i in range(26):
        if ans[i]:
            print(chr(ord('a') + i), end='')
    print()
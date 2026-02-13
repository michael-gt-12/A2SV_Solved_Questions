t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    
    ans = float('inf')
    

    for i in range(n - 1):
        if s[i:i+2] == "aa":
            ans = 2
            break 
    

    if ans > 2:
        for i in range(n - 2):
            sub = s[i:i+3]
            if sub == "aba" or sub == "aca":
                ans = min(ans, 3)
                break
    

    if ans > 3:
        for i in range(n - 3):
            sub = s[i:i+4]
            if sub == "abca" or sub == "acba":
                ans = min(ans, 4)
                break
    
    
    if ans > 4:
        for i in range(n - 6):
            sub = s[i:i+7]
            if sub == "abbacca" or sub == "accabba":
                ans = min(ans, 7)
                break
    
    print(ans if ans != float('inf') else -1)

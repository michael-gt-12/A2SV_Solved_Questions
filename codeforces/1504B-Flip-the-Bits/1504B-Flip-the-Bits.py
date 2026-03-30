t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()
    
    balance = [0] * n
    ones = 0
    zeros = 0
    
    for i in range(n):
        if a[i] == '1':
            ones += 1
        else:
            zeros += 1
        balance[i] = ones - zeros
    
    flip = 0
    possible = True
    
    for i in range(n - 1, -1, -1):
        if flip % 2 == 0:
            current = a[i]
        else:
            current = '1' if a[i] == '0' else '0'
        
        if current == b[i]:
            continue
        
        if balance[i] != 0:
            possible = False
            break
        
        flip ^= 1
    
    print("YES" if possible else "NO")
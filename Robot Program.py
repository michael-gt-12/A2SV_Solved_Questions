t = int(input())
for _ in range(t):
    n, pos, k = map(int, input().split())
    s = input().strip()
    
    time = 0
    count = 0
    curr = pos
    
    first_hit = -1
    
    for i in range(n):
        if time >= k:
            break
        
        if s[i] == 'L':
            curr -= 1
        else:
            curr += 1
        
        time += 1
        
        if curr == 0:
            first_hit = time
            count += 1
            break
    
    if first_hit == -1:
        print(0)
        continue
    
    curr = 0
    cycle_time = -1
    time2 = 0
    
    for i in range(n):
        if s[i] == 'L':
            curr -= 1
        else:
            curr += 1
        
        time2 += 1
        
        if curr == 0:
            cycle_time = time2
            break
    
    if cycle_time == -1:
        print(1)
        continue
    
    remaining = k - first_hit
    count += remaining // cycle_time
    
    print(count)

import sys
input = sys.stdin.readline

n , k = map(int,input().split())
a = list(map(int,input().split()))

k_map = {}
left = 0

max_len = [0,0]

for right in range(n):

    if a[right] in k_map:
        k_map[a[right]] += 1
    else:
        k_map[a[right]] = 1

    while len(k_map) > k:
        if k_map[a[left]] > 1:
            k_map[a[left]] -= 1
        else:
            del k_map[a[left]]
        
        left += 1
    
    if (right - left) > (max_len[1] - max_len[0]):
        max_len[0] = left
        max_len[1] = right

print(max_len[0]+1 , max_len[1]+1)
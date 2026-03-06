from collections import Counter

t = int(input())

for _ in range(t):
    n , k = map(int,input().split())
    stripe = input().strip()

    stripe_count = Counter(stripe[:k])
    change = stripe_count.get("W",0)
    l = 0
    
    for r in range(k,n):
        stripe_count[stripe[r]] += 1
        stripe_count[stripe[l]] -= 1
        l += 1
        change = min(change,stripe_count["W"])
        
    print(change)
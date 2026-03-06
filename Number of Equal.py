from collections import Counter

n , m = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_counter = Counter(a)
b_counter = Counter(b)

count = 0

for key in a_counter:
    count += a_counter[key] * b_counter.get(key,0)

print(count)

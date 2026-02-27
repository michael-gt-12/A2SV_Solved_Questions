n = int(input())
coord = sorted(map(int,input().split()))
if n % 2 == 0:
    print(coord[n//2 - 1])
else:
    print(coord[n//2])

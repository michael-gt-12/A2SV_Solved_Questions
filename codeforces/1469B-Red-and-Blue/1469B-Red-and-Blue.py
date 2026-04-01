t = int(input())

for _ in range(t):
    n = int(input())
    red = list(map(int,input().split()))
    m = int(input())
    blue = list(map(int,input().split()))

    max_red = 0
    red_total = 0
    for num in red:
        red_total += num
        max_red = max(max_red,red_total)

    max_blue = 0
    blue_total = 0
    for num in blue:
        blue_total += num
        max_blue = max(max_blue,blue_total)

    print(max_red + max_blue)
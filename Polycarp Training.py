n = int(input())
contest = list(map(int, input().split()))
contest.sort()
days = 0
for problems in contest:
    if problems >= days + 1:
        days += 1

print(days)

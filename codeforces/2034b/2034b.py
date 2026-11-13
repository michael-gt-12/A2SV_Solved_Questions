# t = int(input())
# for _ in range(t):
#     # take the input and convert the string to a binary list
#     n,m,k = map(int,input().split())
#     s = input()
#     slist = []
#     for char in s:
#         slist.append(int(char))

#     # use sliding window to find the count( the number of times he has to use timar)
#     left = 0
#     right = m
#     total = sum(slist[:m])
#     count = 0
#     if total == 0:
#         count += 1
#         slist[right-1] = 1

#     total = sum(slist[:m])

#     while right < n:
#         total -= slist[left]
#         left += 1
#         total += slist[right]
#         if total == 0:
#             slist[right] = 1
#             count += 1
#         right += 1

#     print(count)


t = int(input())
for _ in range(t):
    # take the input and convert the string to a binary list
    n,m,k = map(int,input().split())
    s = input()
    slist = []
    for char in s:
        slist.append(int(char))

    # use sliding window to find the count( the number of times he has to use timar)
    left = 0
    right = m
    total = sum(slist[:m])
    count = 0
    
    last_op_end = -1

    if total == 0:
        if (right - 1) > last_op_end:
            count += 1
            last_op_end = (right - 1) + k - 1
            for idx in range(right - 1, min(n, last_op_end + 1)):
                slist[idx] = 1
            total = sum(slist[left:right])

    while right < n:
        total -= slist[left]
        left += 1
        total += slist[right]
        
        if total == 0:
            if right > last_op_end:
                count += 1
                last_op_end = right + k - 1
                for idx in range(right, min(n, last_op_end + 1)):
                    slist[idx] = 1
                total = sum(slist[left:right+1])
                
        right += 1

    print(count)
s = input().strip()

stack = []
last_invalid = -1
max_len = 0
count = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        if stack:
            stack.pop()

            if stack:
                length = i - stack[-1]
            else:
                length = i - last_invalid

            if length > max_len:
                max_len = length
                count = 1
            elif length == max_len:
                count += 1
        else:
            last_invalid = i

if max_len == 0:
    print("0 1")
else:
    print(max_len, count)
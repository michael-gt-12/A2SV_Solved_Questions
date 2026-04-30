from collections import defaultdict

n = int(input())
array = []

for _ in range(n-1):
    array.append(int(input()))

tree = defaultdict(list)

for i in range(len(array)):
    tree[array[i]].append(i+2)

for key in tree:
    count = 0
    ind = 0
    value = tree[key]
    while count < 3 and ind < len(value):
        if value[ind] not in tree:
            count += 1
        ind += 1

    if count < 3:
        print("No")
        break
else:
    print("Yes")
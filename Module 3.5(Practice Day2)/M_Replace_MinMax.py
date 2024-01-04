n = int(input())
a = list(map(int, input().split()))
max_idx = int(a.index(max(a)))
min_idx = int(a.index(min(a)))

maxVal = int(max(a))
minVal = int(min(a))

a[min_idx] = maxVal
a[max_idx] = minVal

for i in a:
    print(i, end= " ")
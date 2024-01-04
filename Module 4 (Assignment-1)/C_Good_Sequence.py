n = int(input())
v = list(map(int, input().split()))
mp = {}
for i in v:
    mp[i] = mp.get(i, 0) + 1

st = set(v)

cnt = 0
for x in st:
    if mp[x] != x:
        if x > mp[x]:
            cnt += mp[x]
        else:
            cnt += mp[x] - x

print(cnt)

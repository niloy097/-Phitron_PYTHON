a, b = input().split()
x = (int)(a)
y = (int)(b)
cnt = 0
for i in range(x+1):
    for j in range(x + 1):
        for k in range(x + 1):
            if(i + j + k == y):
                cnt += 1


print(cnt)
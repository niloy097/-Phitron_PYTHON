t = (int)(input())
for _ in range(t):
    x, y = (input().split())
    a = (int)(x)
    b = (int)(y)
    if(a > b):
        a, b = b, a
    sum = 0
    for i in range(a+1, b):
        if(i % 2 != 0):
            sum += i
    print(sum)
x, y = (input().split())

a = (int)(x)
b = (int)(y)

sum = 0
for i in range(2, b + 1):
    if(i % 2 == 0):
        sum += (a ** i)
print(sum)
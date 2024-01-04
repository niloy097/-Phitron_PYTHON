a = list(input().split())
for i in range(0, len(a)):
    a[i] = a[i][::-1]

for i in range(0, len(a)):
    if(i == len(a) - 1):
        print(a[i])
        break
    print(a[i], end= " ")
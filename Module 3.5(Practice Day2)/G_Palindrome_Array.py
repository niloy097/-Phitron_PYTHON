n = int(input())
a = list(map(int, input().split()))
b = a[::-1]
# flag = True
# for i in range(0, n):
#     if(a[i] != b[i]):
#         flag = False
#         break
if a == b:
    print("YES")
else:
    print("NO")
n, q = input().split()

n = int(n)
q = int(q)

a = list(map(int, input().split()))
b = a

for i in range(1, n):
    b[i] = b[i - 1] + a[i]
    
for _ in range(q):
    l, r = input().split()
    l = int(l)
    r = int(r)
    l = l - 1
    r = r - 1
    if(l == 0):
        print(b[r])
    else:
        print(b[r] - b[l-1])
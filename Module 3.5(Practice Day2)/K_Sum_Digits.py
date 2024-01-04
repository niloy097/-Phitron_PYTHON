n = int(input())
string = input()
a = (list(string))
sum  = 0
for i in range(0, n):
    sum = sum + int(a[i])

print(sum)
n = (int)(input())
print(0, 1, end=" ")
first = 0
second = 1
for i in range(1, n - 1):
    fib = first + second
    if i == n - 2:
        print(fib)
        continue
    print(fib, end=" ")
    first = second
    second = fib
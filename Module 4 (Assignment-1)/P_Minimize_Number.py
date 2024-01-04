n = int(input())
arr = list(map(int, input().split()))
bool = True
for i in arr:
    if(i % 2 != 0):
        bool = False
        break

if bool == False:
    print(0)
else:
    mn = 1000000007
    for i in arr:
        cnt = 0
        while(True):
            if i % 2 == 0:
                cnt += 1
            i /= 2
            if(i == 0 or i % 2 != 0):
                break
        mn = min(mn, cnt)
    print(mn)
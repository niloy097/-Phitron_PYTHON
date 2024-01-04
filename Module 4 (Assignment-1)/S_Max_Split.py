list = input()
cnt_l = 0
cnt_r = 0
sepp = ""
lStr = []
for i in list:
    sepp += i
    if i == 'R':
       cnt_r += 1
    else:
       cnt_l += 1
    if cnt_l == cnt_r:
        lStr.append(sepp)
        sepp = ""
        cnt_l = 0
        cnt_r = 0

print(len(lStr))
for i in lStr:
    print(i)


# a = "Naeem Biswass"
# a += "b"
# for i in a:
#     print(i, end="")
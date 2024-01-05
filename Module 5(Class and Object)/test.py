list = []

a = dict(name = 'niloy', age = 23, is_student = True)
b = dict(name = "Nabid", age = 22, is_student = False)
x = dict(name = "Sunny", age = 18, is_student = True)
c = dict(name = "Mow", age = 23, is_student = True)

list.append(a)
list.append(b)
list.append(x)
list.append(c)
get_idx = -1
for ele in list:
    if ele["name"] == "Sunny":
        get_idx += 1
        break
    else:
        get_idx += 1
print(get_idx)

list.remove(list[get_idx])
print(list)
def multip():
    return 3, 4 #return things as tuple if we use just comma
print(multip())


thigs = 'pen', 'tripod', 'Water bottle', 'charger', 'phone', 'web cam'
# print(type(thigs))

# print(thigs[0])
# print(thigs[-2])
# print(thigs[2:6])


if "phone" in thigs:
    print("Exists")  
for item in thigs:
    print(item)
# thigs[0] = "niloy"
print(thigs) #illegal
mega = ([23, 34, 3], [23, 56, 2])
print(mega)

mega[0][2] = 234

print(mega)
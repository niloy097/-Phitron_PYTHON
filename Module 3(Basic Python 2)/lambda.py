# def doubleIT(x):
#     return x * 2

# print(doubleIT(2))

#makig short this fucntion-->

#one parameter
# doubleIt = lambda x : x * 2
# squreIt = lambda x : x * x

# print(doubleIt(4))
# print(squreIt(2))


# #multiple parameter-->
# add = lambda x, y, z : x + y + z
# print(add(4, 2, 3))
# #map-->
# num = [1, 2, 3, 4]
# # doubled_nums = map(doubleIt, num)
# double_nums = map(lambda x : x * 2, num)
# squred_nums = map(lambda x : x * x, num)
# print(num)
# print(list(double_nums))
# print(list(squred_nums))


actors = [
    
    {'name' : 'sabana', 'age' : 45},
    {'name' : 'sabnoor', 'age' : 45},
    {'name' : 'akji', 'age' : 23},
    {'name' : 'df', 'age' : 43},
    {'name' : 'niloy', 'age' : 23},
]
# print(actors)
# juniors = filter(lambda actor : actors['age'] < 40, actors)

# print(list(juniors))

jun = filter(lambda x : x['age'] < 40, actors)

print(list(jun))
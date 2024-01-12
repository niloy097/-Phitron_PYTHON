import math 
def timer(func):
    def inner(*args, **kwargs):
        print("Time Started")
        # print(func)
        func(*args, **kwargs)
        print("Time ended")
    return inner

# timer()()
@timer
def get_factorial(n):
    print("Factorial Starting")
    result = math.factorial(n)
    print(f"Factorial of {n} is: {result}")

get_factorial(n = 120)

# #general way to decorate
# def get_factorial():
#     print("Factorial starting")

# timer(get_factorial)()
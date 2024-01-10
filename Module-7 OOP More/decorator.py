def timer():
    def inner():
        print("Time Started")
        
        print("Time ended")
    return inner

# timer()()

@timer()
def get_factorial():
    print("Factorial Starting")


get_factorial()


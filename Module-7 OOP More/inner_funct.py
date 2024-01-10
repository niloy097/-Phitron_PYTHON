#function is a first class object

def double_decker():
    print("Starting the double decker")
    def inner_func():
        print("Inside the inner")
        return 3000
    return inner_func

# print(double_decker())
# print(double_decker()())

def do_something(work):
    print("Work Started")
    # print(work)
    work()
    print("Work ended")

# do_something(2)
# do_something("Ami Bussy")

def coding():
    print("coding in python")
    
# do_something(coding)

def sleeping():
    print("Seeping and Dreaming in python")
    
do_something(sleeping)
    
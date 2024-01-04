def sum(num1, num2, num3 = 0, num4 = 0, num5 = 0):
    res = num1 + num2 + num3 + num4 + num5
    return res


total = sum(10, 20, 30)

print(total)

#args

def all_sum(num1, num2, *numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum += num
    return sum
    
total = all_sum(10, 56, 89, 11)
print("All sum : ", total)
numbers = [45, 87, 65, 43, 85, 14, 26, 61]
odds = []

for num in numbers:
    if num % 2 == 1:
        odds.append(num)
    
print(odds)

even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)

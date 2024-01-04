def full_name(first, last):
    name = f'{first} {last}'
    return name


#take parame. in order
# name = full_name("Alu", "Kodu")

# print(name)


#without order
# name = full_name(last = "Lodu", first = "Alu")
# print(name)


# def famous_name(first, last, **additonal):
#     name = f'{first} {last}'
#     print(additonal["title"])
#     for key, value in additonal.items():
#         print(key, value)
#     return name


# name = famous_name(first="Taher", last = "Ali", title= "Hujur", additonal="Sayekh")
# print(name)



#multiple return
def a_lot(num1, num2):
    sum = num1 + num2
    num = num1 * num2
    rem = num1 % num2
    # return sum, num, rem
    return [sum, num, rem]



everything = a_lot(55, 21)
print(everything)
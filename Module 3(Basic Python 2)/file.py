#.csv comma seperated value
#.txt text file

# with open("Tex.txt", "w") as file:
#     file.write("I love Python!")
# with open("Tex.txt", "a") as file:
#     file.write(" I love Python!")


with open("Tex.txt", "r") as file:
    text = file.read()
    print(text)
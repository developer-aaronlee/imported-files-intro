# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# with open("my_file.txt", mode="w") as file:
#     file.write("Hello World")

with open("my_file.txt", mode="a") as file:
    file.write(f"\nHELLO WORLD")

with open("new_file", mode="w") as file:
    file.write("hello hello")
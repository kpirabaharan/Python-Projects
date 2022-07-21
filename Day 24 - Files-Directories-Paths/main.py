# Don't need to close the file with with ... as ... :
# Mode r (default) read-only, w overwrites, a appends
with open("my_file.txt", mode="w") as file:
    contents = file.read()
    print(contents)


# Inefficient way of opening and reading a file

# file = open("my_file.txt")
#
# contents = file.read()
# print(contents)
#
# file.close()

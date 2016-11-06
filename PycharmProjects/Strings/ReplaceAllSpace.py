"""write a method to replace all space in a string with '%20'
"""

# using a list to store each char and change space to '%20', then join list into a string
def ReplaceAllSpace(str):
    charlist = []

    for char in str:
        if char == " ":
            char = '%20'

        charlist.append(char)

    return ''.join(charlist)

print(ReplaceAllSpace(" Smith    q m "))



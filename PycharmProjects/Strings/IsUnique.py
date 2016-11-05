teststring = "abcdefa"

def unique(string):
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # char already found in string
            return False
        char_set[val] = True

    return True


print(unique(teststring))

def compress(str1):
    count = 0
    res = []
    prev = str1[0]

    for char in str1:
        if char == prev:
            count += 1

        else:
            res += prev + str(count)
            prev = char
            count = 1

    res += prev + str(count)
    res = ''.join(res)
    if len(res) < len(str1):
        return res
    else:
        return str1


print (compress("aabcccaaa"))

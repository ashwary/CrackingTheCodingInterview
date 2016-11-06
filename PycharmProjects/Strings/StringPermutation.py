

def isPermutationSort(s1, s2):
    # sort both strings, check if they are equal
    if len(s1) != len(s2): return False
    return sorted(s1) == sorted(s2)

print(isPermutationSort("abc", "cbd"))
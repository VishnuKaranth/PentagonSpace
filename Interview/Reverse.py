def reverse_list(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

print(reverse_list("Hello"))  # Output: "olleH"


def recursive_reverse(s):
    if len(s) == 0:
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]
    
print(recursive_reverse("Hello"))  # Output: "olleH"
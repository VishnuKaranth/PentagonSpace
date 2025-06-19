def swapcase(s1):
    nstr = ""
    for i in range(len(s1)):
        if 'a' <= s1[i] <= 'z':
            nstr += chr(ord(s1[i]) - 32)
        elif 'A' <= s1[i] <= 'Z':
            nstr += chr(ord(s1[i]) + 32)
        else:
            nstr += s1[i]
    return nstr

s1 = input("Enter a string: ")
print("Original string:", s1)
s1 = swapcase(s1)
print("Updated String:", s1)
 
# The ASCII code for a is 97 and for A is 65.
# The ASCII code for 0 is 48 and for 9 is 57.

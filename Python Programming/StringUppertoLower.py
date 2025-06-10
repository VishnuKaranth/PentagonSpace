def touppercase(s1):
    nstr = ""
    for i in range(len(s1)):
        if 'a' <= s1[i] <= 'z':
            nstr += chr(ord(s1[i]) - 32)
        else:
            nstr += s1[i]
    return nstr

def tolowercase(s1):
    nstr = ""
    for i in range(len(s1)):
        if 'A' <= s1[i] <= 'Z':
            nstr += chr(ord(s1[i]) + 32)
        else:
            nstr += s1[i]
    return nstr
s1 = input("Enter a string: ")
print("Original string:", s1)
s1 = touppercase(s1)
print("Uppercase string:", s1)
s1 = tolowercase(s1)
print("Lowercase string:", s1)
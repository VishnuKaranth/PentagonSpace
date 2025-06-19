def fiterpangram(s):
    nstr = ""
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            nstr += chr(ord(s[i]) + 32)
        elif 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
            nstr = nstr + s[i]
    return nstr

def ispangram(s):
    s = fiterpangram(s)
    ascii = [0] * 26
    if len(s) < 26:
        return False
    for i in range(len(s)):
        ascii[ord(s[i]) - 97] += 1
    for i in ascii:
        if i == 0:
            return False
    return True



s = input("enter a string:")
if ispangram(s):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
    
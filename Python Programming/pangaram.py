def anpanagramfiltrations(s):
    nstr = ""
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            nstr += chr(ord(s[i]) + 32)
        elif 'a' <= s[i] <= 'z' or '0' <= s[i] <= '9':
            nstr += s[i]
    return nstr

def ispanagram(s1, s2):
    s1 = anpanagramfiltrations(s1)
    s2 = anpanagramfiltrations(s2)
    if len(s1) != len(s2):
        return False
    ascii = [0] * 26
    for i in range(len(s1)):
        ascii[ord(s1[i]) - 97] += 1
        ascii[ord(s2[i]) - 97] -= 1
        
    for i in range(len(ascii)):
        if ascii[i] != 0:
            return False
    return True
s1 = input("Enter string1: ")
s2 = input("Enter string2: ")
flag = ispanagram(s1, s2)
if flag:
    print("String is an anagram")
else:
    print("String is not an anagram")
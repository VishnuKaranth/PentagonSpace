def palindromefiltration(s):
    nstr = ""
    for i in range(0, len(s)):
        if 'A' <= s[i] <= 'Z':
            nstr = nstr + chr(ord(s[i]) + 32)
        elif 'a' <= s[i] <= 'z'or '0' <= s[i] <= '9':
            nstr = nstr + s[i]
    return nstr

def ispalindrome(s):
    s = palindromefiltration(s)
    i , j = 0, len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

s = input("Enter a string: ")
if ispalindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")          
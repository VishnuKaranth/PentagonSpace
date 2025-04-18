#Integer Palindrome
def is_palindrome(s):
    temp = s
    rev = 0
    if s < 0:
        s = s * -1
    while s != 0:
        rem = s % 10
        rev = (rev * 10) + rem
        s = s // 10
    if temp < 0:
        rev = rev * -1
    return rev

    
s = int(input("Enter a number: "))
pali = is_palindrome(s)
if pali == s:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
    
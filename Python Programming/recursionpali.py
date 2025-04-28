#Integer Palindrome
def is_palindrome(s,rev,temp):
    if s <= 0:
        return rev == temp
    while s != 0:
        rem = s % 10
        rev = (rev * 10) + rem
        s = s // 10
        return is_palindrome(s,rev,temp)

    
s = int(input("Enter a number: "))
is_palindrome(s,0,temp=s)
if is_palindrome:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
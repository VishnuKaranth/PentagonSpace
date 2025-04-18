#First n palindromic numbers
def is_palindrome(s):
    temp = s
    rev = 0
    if s < 0:
        s = s * -1
    while s != 0:
        rem = s % 10
        rev = (rev * 10) + rem
        s //= 10
    if temp < 0:
        rev = rev * -1
    return temp == rev

n = int(input("Enter a number: "))
count = 0
i = 1
print("The palindomic numbers of first ", n, "are:")
while i <= n:
    yolo = is_palindrome(i)
    if yolo:
        print(i)
        count += 1
    i = i + 1


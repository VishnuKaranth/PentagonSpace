def reverse_string(s):
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

n1 = int(input("Enter start of range: "))
n2 = int(input("Enter end of range: "))

for num in range(n2, n1-1, -1):
    print(reverse_string(num), end=" \n")

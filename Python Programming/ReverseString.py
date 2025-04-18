# def reverse_string(s):
#     temp = s
#     rev = 0
#     if s < 0:
#         s = s * -1
#     while s != 0: 
#         rem = s % 10
#         rev = (rev * 10) + rem
#         s = s // 10
#     if temp < 0:
#         rev = rev * -1
#     return rev

# n = int(input("Enter a number: "))
# yolo = reverse_string(n)
# print("Reverse of", n, "is", yolo)

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

n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
for i in range(n1, n2+1):
    rev = reverse_string(i)
    print("Reverse of", i, "is", rev)
# def non_pali(n):
#     temp = n
#     rev = 0
#     if n < 0:
#         n = n * -1
#     while n != 0:
#         rem = n % 10
#         rev = (rev * 10) + rem
#         n = n // 10
#     if temp < 0:
#         rev = rev * -1
#     if temp == rev:
#         return True
#     else:
#         return False
    
# n = int(input("Enter a number: "))
# count = 0
# i = 1
# while i <= n:
#     yolo = non_pali(i)
#     if yolo == False:
#         print(i)
#         count += 1
#     i = i + 1

terms = int(input("Enter the number"))
n1 = 0
n2 = 1
if terms
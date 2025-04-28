# n = int(input("Enter a number: "))
# count = 0
# countloops = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1
#         print(i)
#     countloops += 1

# print("The number of factors of ", n, "is: ", count)
# print("The number of loops is: ", countloops)


# Finding factors of a number using minimum loops

# for i in range(1, int(n**0.5) + 1):
#     if n % i == 0:
#         count += 1
#         print(i)
#         if i != n // i:
#             print(n // i)
#     countloops += 1


# n = int(input("Enter a number: "))
# count = 0
# countloops = 0
# i = 1
# while i * i <= n:
#     if n % i == 0:
#         print(i)
#         count += 1
#         val = (n//i)
#         if i != val:
#             print(val)
#     i += 1
#     countloops += 1
# print("The number of factors of ", n, "is: ", count*2)
# print("The number of loops is: ",countloops)

#using def

# def dis_factors(n):
#     i = 1
#     while i * i <= n:
#         if n % i == 0:
#             print(i)
#             val = (n//i)
#             if i != val:
#                 print(val)
#         i += 1
#     return 0
# n = int(input("Enter a number: "))
# dis_factors(n)


            

        

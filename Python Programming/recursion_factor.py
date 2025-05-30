# def recr_factor(n,i):
#     if i * i > n:
#         return
#     if n % i == 0:
#         print(i)
#         val = (n//i)
#         if i != val:
#             print(val)
#     recr_factor(n, i+1)

# n = int(input("Enter a number: "))
# recr_factor(n,1)

#Prime Factorization using Recursion
def prime(n,i,count):
    if (i * i) > n:
        return count == 2
    if n % i == 0:
        count += 1
        if i != n//i:
            count += 1
    return prime(n,i+1,count)
    

n = int(input("Enter a number: "))
prime(n,0,0)
            
        
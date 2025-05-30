#Assignment 1
# def printnum(n):
#     if n <= 0:
#         return
#     print(n)
#     printnum(n-1)
#     print(n)
    
# n = int(input('Enter the number'))
# printnum(n)

# Assignment 2
# def printnum(n, i):
#     if n <= 0:
#         return
#     if i <= n:
#         print(i)
#         printnum(n, i+1)
#     else:
#         print(n)
#         printnum(n-1, n)

# n = int(input('Enter the number'))
# printnum(n, i=1)

# def add(a,b):
#     print(a+b)
# n = 10
# m = 20
# add(n,m)
    
def fibonacci(nterms):
    sequence = []
    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        return "Please enter a positive integer"
    elif nterms == 1:
        sequence.append(n1)
    else:
        while count < nterms:
            sequence.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    return sequence

# main program
nterms = int(input("How many terms? "))
result = fibonacci(nterms)

if isinstance(result, str):  # check if it's an error message
    print(result)
else:
    print("Fibonacci sequence:", result)

    
    
    
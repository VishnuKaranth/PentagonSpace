#Prime Numbers
def is_prime(num):
    count = 0
    if num <= 1:
        return False
    i = 1
    while i * i <= num:
        if num % i == 0:
            val = (num // i)
            count += 1
            if i != val:
                count += 1
        if count > 2:
            return False
        i += 1
    return count == 2

# n = int(input("Enter a number: "))
# pun = is_prime(n)
# if pun:
#     print(n, "is prime")
# else:
#     print(n, "is not prime")
    
#Print only prime numbers for a defined range

# n1 = int(input("Enter start of range: "))
# n2 = int(input("Enter end of range: "))

# for num in range(n1, n2+1):
#     if is_prime(num):
#         print(num, end=" ")
        
#Print non prime numbers for a defined range
# n1 = int(input("Enter start of range: "))
# n2 = int(input("Enter end of range: "))

# for num in range(n1, n2+1):
#     if not is_prime(num):
#         print(num, end=" ")
        
#Print the first n prime numbers
n = int(input("Enter a number: "))
count = 0
i = 1
print("The first ", n, "prime numbers are:")
while count < n:
    if is_prime(i):
        print(i)
        count += 1
    i += 1
    
#Fibonacci
#GCD
#LCM
#Co-Primes

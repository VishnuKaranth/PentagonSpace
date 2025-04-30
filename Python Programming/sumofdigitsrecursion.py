#sum of digits using recursion
def sum_of_digits(n,sum):
    if n == 0:
        return 0
    rem = n % 10
    n = n // 10
    sum = rem + n
    return sum_of_digits(n,sum)

n = int(input("Enter a number:"))
ans = sum_of_digits(n, sum)
print(ans)
    
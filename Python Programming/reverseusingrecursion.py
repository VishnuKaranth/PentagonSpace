def reverse(n,rev):
    if n<=0:
        return rev
    rem = n % 10
    rev = (rev*10) + rem
    n = n // 10
    return reverse(n,rev)

n = int(input("Enter a number "))
g =reverse(n,0)
print(g)    
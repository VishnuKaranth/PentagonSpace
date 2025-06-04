# This is a simple program to demonstrate the use of lists in Python
# It allows the user to input 5 numbers and stores them in a list
# Finally, it prints the numbers in the list
arr = []
i = 0
while i < 5:
    val = int(input("Enter a number: "))
    arr.insert(i, val)
    i += 1
    
for num in arr:
    print(num)
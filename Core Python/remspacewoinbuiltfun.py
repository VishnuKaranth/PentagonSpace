str = input("Enter a string: ")
i = 0
newstr = " "
while(i<=len(str)-1):
    data = str[i]
    if (data == " "):
        i = i + 1
    else:
        newstr = newstr + data
        i = i + 1
print(newstr)
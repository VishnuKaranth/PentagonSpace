# def swap(inp):
#     return inp.swapcase()

# if __name__ == "__main__":
#     inp = input("Enter a string: ")
#     result = swap(inp)
#     print("Converted string:", result)

# str = input("Enter a string")
# str1 = str.upper()
# str2 = str.lower()
# str3 = str.swapcase()
# print(str1)
# print(str2)
# print(str3)


str = input("Enter a string: ")
i = 0
newstr = " "
while(i<=len(str)-1):
    data = str[i]
    ascii = ord(data)
    if(ascii>=65 and ascii<=90):
        newscii = ascii+32
        convchar = chr(newscii)
        newstr = newstr + convchar
    else:
        newscii = ascii-32
        convchar = chr(newscii)
        newstr = newstr + convchar
    i+=1
print(newstr)
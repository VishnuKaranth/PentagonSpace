# str = input("Enter anything:")
# print(str)
# str1 = str.lstrip()
# print(str1)
# str2 = str.rstrip()
# print(str2) 
# str3 = str.strip()
# print(str3)

str = input("Enter anything:")
print("Original string:", str)

i = 0
while i < len(str) and str[i] == ' ':
    i += 1
str1 = str[i:]
print("Removing leading spaces:", str1)

j = len(str1) - 1
while j >= 0 and str1[j] == ' ':
    j -= 1
str2 = str1[:j + 1]
print("Removing trailing spaces:", str2)
print("emoving both leading and trailing spaces:", str2)

str_no_spaces = ""
for char in str:
    if char != ' ':
        str_no_spaces += char
print("After removing all white spaces:", str_no_spaces)
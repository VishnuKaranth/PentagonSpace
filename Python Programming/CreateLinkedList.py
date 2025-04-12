# s1 = "abbcde"
# for i in range (0, len(s1)):
#     print(i)
    
# print("================")
# for i in s1:
#     print(i)

# s1 = "abbcde"
# for i in range(0, len(s1)):
#     print("index: n ", i, "char: ", s1[i])
    
# print("================")
# for i in s1:
#     print("index:", s1.index(i), "char: ", i)


s1 = "abbcde"
print("Reading in forward direction: ")
for i in range(0, len(s1)):
    print("index: ", i, "char: ", s1[i])
print("Reading in reverse direction: ")
for i in range(len(s1)-1, 0-1, -1):
    print("index: ", i, "char: ", s1[i])
    
    
print("================")
for i in s1:
    print("index:", s1.index(i), "char: ", i)
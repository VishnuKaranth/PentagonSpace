#String are immutable in Python, meaning that once a string is created, it cannot be modified.
# However, you can create a new string based on the original one.
# Lists, on the other hand, are mutable, meaning you can change their contents without creating a new object.
# String objects are im


l1 = [1,2,3,4]
print(l1)
print(id(l1))
l1[0] = l1[0] + 5
print(l1)
print(id(l1))

s1 = "abc"
print(s1)
print(id(s1))
s1 = s1 + "d"
print(s1)
print(id(s1))

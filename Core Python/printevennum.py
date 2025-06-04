def evenum(elements):
    for num in elements:
        if num % 2 == 0:
            print(num)

num_ele = int(input("Enter the number of elements: "))
elements = []
for i in range(num_ele):
    elements = int(input("Enter the elements: "))
evenum(elements)
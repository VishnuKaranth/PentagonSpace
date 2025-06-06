#LeetCode 162: Find Peak Element
def createListandTarget():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers:"))
            l1.append(num)
        except Exception as e:
            target = int(input("Enter the target number to search: "))
            return l1, target


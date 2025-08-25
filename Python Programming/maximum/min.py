def createlist():
    l1 = []
    while True:
        try:
            n = int(input("Enter a number (0 to stop): "))
            l1.append(n)
        except Exception as e:
            return l1
        
def max_min(arr):
    if not arr:
        return None, None
    max_val = arr[0]
    min_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

arr = createlist()
max_val, min_val = max_min(arr)

print("Maximum value:", max_val)
print("Minimum value:", min_val)
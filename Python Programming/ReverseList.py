def reverse_list(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
arr = [5,4,3,2,1]
print("Original list:", arr)
reverse_list(arr)
print("Reversed list:", arr)


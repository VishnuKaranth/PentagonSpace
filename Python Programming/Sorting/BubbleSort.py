def crete_list():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers: "))
            l1.append(num)
        except Exception as e:
            
            return l1

def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = crete_list()

print("Unsorted array: ", arr)
print("Ascending Sorted Array using Bubble Sort", bubble_sort_asc(arr))
print("Descending Sorted Array using Bubble Sort", bubble_sort_desc(arr))
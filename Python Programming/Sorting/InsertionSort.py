def crete_list():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers: "))
            l1.append(num)
        except Exception as e:
            
            return l1
    
def insertion_sort(arr):
    n = len (arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr

arr = crete_list()
print("Unsorted array: ", arr)
print("Sorted Array using Insertion Sort", insertion_sort(arr))
        
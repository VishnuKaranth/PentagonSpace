def crete_list():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers: "))
            l1.append(num)
        except Exception as e:
            
            return l1

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = crete_list()
print("Unsorted array: ", arr)
print("Sorted Array using Selection Sort", selection_sort(arr))
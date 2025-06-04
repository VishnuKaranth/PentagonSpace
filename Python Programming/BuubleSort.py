def createlist():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers: "))
            l1.append(num)
        except Exception as e:
            return l1

def bubbleSortdes(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubbleSortasc(arr):
    n = len(arr)
    for i in range(0, n-1):
        #swap = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = createlist()
print("Unsorted array: ", arr)
print("Ascending Sorted Array using Bubble Sort",bubbleSortasc(arr))
print("Descending Sorted Array using Bubble Sort",bubbleSortdes(arr))
def createlist():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers: "))
            l1.append(num)
        except Exception as e:
            return l1

def insertionsortasc(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr

def insertionsortdsc(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] > arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr

arr = createlist()
print("Unsorted array: ", arr)
sorted_arracsc = insertionsortasc(arr)
print("Sorted array using Insertion Sort in Ascending Order: ", sorted_arracsc)
sorted_arrdsc = insertionsortdsc(arr)
print("Sorted array using Insertion Sort in Descending Order: ", sorted_arrdsc)
    
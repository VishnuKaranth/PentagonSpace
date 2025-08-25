def crete_list():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers: "))
            l1.append(num)
        except Exception as e:
            
            return l1
    
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge_sort(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = crete_list()
print("Unsorted array: ", arr)
print("Sorted Array using Merge Sort", merge_sort(arr))


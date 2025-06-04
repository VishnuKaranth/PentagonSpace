def createListandTarget():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers:"))
            l1.append(num)
        except Exception as e:
            target = int(input("Enter the target number to search: "))
            return l1, target


def binarySearchasc(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end ) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def binarySearchdsc(arr,target):
    start = 0 
    end = len(arr) - 1 
    while start <= end:
        mid = (start + end ) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1
     
arr, target = createListandTarget()
# binarysearchasc = binarySearchasc(arr, target)
# print ("Element found at index in ascending order: ", binarysearchasc)
# binarySearchdesc = binarySearchdsc(arr, target)
# print ("Element found at index in descending order: ", binarySearchdesc)
if arr[0] < arr[-1]:
    binarysearchasc = binarySearchasc(arr, target)
    print ("Element found at index in ascending order: ", binarysearchasc)
else:
    binarySearchdesc = binarySearchdsc(arr, target)
    print ("Element found at index in descending order: ", binarySearchdesc)
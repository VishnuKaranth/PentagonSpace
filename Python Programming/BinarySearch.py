#Time Complexity of Binary Search is O(log n)
# Space Complexity of Binary Search is O(1)
# Binary Search is used to search an element in a sorted array.
# It works by repeatedly dividing the search interval in half.


def createListandTarget():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers:"))
            l1.append(num)
        except Exception as e:
            target = int(input("Enter the target number to search: "))
            return l1, target


def orderagnosticbinarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    if arr[start] < arr[end]:
        flag = True #for ascending order
    else:
        flag = False #for descending order
    while start <= end:
        mid = (start + end ) // 2
        if target == arr[mid]:
            return mid
        if flag:
            #Ascending order
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else: 
            #Descending order
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

# def binarySearchdsc(arr,target):
#     start = 0 
#     end = len(arr) - 1 
#     while start <= end:
#         mid = (start + end ) // 2
#         if target == arr[mid]:
#             return mid
#         elif target > arr[mid]:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return -1
     
arr, target = createListandTarget()
# binarysearchasc = binarySearchasc(arr, target)
# print ("Element found at index in ascending order: ", binarysearchasc)
# binarySearchdesc = binarySearchdsc(arr, target)
# print ("Element found at index in descending order: ", binarySearchdesc)
index = orderagnosticbinarySearch(arr, target)
print("Element found at index: ", index)
if index == -1:
    print("Element not found in the list.")

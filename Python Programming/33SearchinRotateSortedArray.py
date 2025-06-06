def reverse_list(arr, i , j):
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    
def rotate_array(arr, k):
    n = len(arr)
    #Step 1: Reverse the entire array
    reverse_list(arr, k, n - 1)
    #Step 2: Reverse the first k elements  
    reverse_list(arr, 0, k - 1)
    #Step 3: Reverse the remaining n-k elements
    reverse_list(arr, 0, n - 1) 

arr = [1,2,3,4,5]
k = 3
if k >= len(arr):
    k = k % len(arr)
print("Original array:", arr)
rotate_array(arr, k)
print("Rotated array:", arr)
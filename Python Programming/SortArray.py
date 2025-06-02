def createlist():
    l1 = []
    while True:
        try:
            num = int(input("Enter numbers: "))
            l1.append(num)
        except Exception as e:
            return l1

def arrAsc(arr1,arr2):
    res = []
    i, j = 0, 0
    n1 = len(arr1)
    n2 = len(arr2)
    
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    # Extra values for arr1          
    while i < n1:
        res.append(arr1[i])
        i += 1
    # Extra values for arr2
    while j < n2:
        res.append(arr2[j])
        j += 1  
    return res

print("Enter elements for for first array: ")
arr1 = createlist()
print("Enter elements for second array: ")
arr2 = createlist()
res = arrAsc(arr1, arr2)
print("Sorted array in ascending order: ", res)        
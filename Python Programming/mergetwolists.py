def merge_lists(l1, l2):
    merged_list = []
    i = j = 0
    
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            merged_list.append(l1[i])
            i += 1
        else:
            merged_list.append(l2[j])
            j += 1
            
    merged_list.extend(l1[i:])
    merged_list.extend(l2[j:])
    return merged_list

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_lists(list1, list2)
print("Merged List:", result)
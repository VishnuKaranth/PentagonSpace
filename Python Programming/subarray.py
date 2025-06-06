#Print all the subarrays of a given array
# def subarrays(arr):
#     n = len(arr)
#     for i in range(n):
#         res = []
#         for j in range(i, n):
#             res.append(arr[j])
#             print(res)

# arr = [1, 2, 3, 4, 5]
# subarrays(arr)

#Program to display the max sum formed out of subarray

# arr = [1, 2, 3, 4, 5]
# n = len(arr)
# max_sum = 0
# for i in range(0,n):
#     res = []
#     sum = 0
#     for j in range(i, n):
#         res.append(arr[j])
#         sum = sum + arr[j]
#         if max_sum < sum:
#             max_sum = sum
# print(max_sum)


#Program to display the min sum formed out of subarray
arr = [1, 2, 3, 4, 5]
n = len(arr)
min_sum = 2**31
for i in range(0,n):
    res = []
    sum = 0
    for j in range(i, n):
        res.append(arr[j])
        sum = sum + arr[j]
        if min_sum > sum:
            min_sum = sum
print(min_sum)
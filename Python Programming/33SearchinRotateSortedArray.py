nums = [4,5,6,7,0,1,2]
target = 0
def reverse_list(nums , target):
    st, en = 0, len(nums) - 1
    while st <= en:
        mid = (st + en) // 2
        if target == nums[mid]:
            return mid
        if nums[st] <= nums[mid]:
            if nums[st] <= target <= nums[mid]:
                en = mid - 1
            else:
                st = mid + 1
        else:
            if nums[mid] <= target <= nums[en]:
                st = mid + 1
            else:
                en = mid - 1
    return -1

index = reverse_list(nums, target)
if index != -1:
    print(f"Element {target} found at index {index}")
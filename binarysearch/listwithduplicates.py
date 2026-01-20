def find_min_with_duplicates(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < arr[high]:
            high = mid
        elif arr[mid] > arr[high]:
            low = mid + 1
        else:
            high -= 1

    return low

#test cases
arr = [4, 5, 6, 1, 1, 1, 2, 3]
print(find_min_with_duplicates(arr))
# Expected output: 3
arr = [10]
print(find_min_with_duplicates(arr))
# Expected output: 0

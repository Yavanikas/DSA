"""so there's a rotated sorted array , we need to 
find the minimum number of times it has been rotated"""
#linear search
def  find(arr):
    pos=0
    for i in range(1,len(arr)):
        if arr[i]<=arr[i-1]:
            return i 
    return pos

#test cases:
print(find([4,5,6,7,0,1,2]))  # 4
print(find([1,2,3,4,5]))      # 0
print(find([10]))             # 0
print(find([3,4,5,1,2]))      # 3

#binary search to reduce inefficiency
def find_rotations_binary(arr):
    if not arr:
        return 0

    beg, end = 0, len(arr) - 1

    while beg <= end:

        # Case 1: array is already sorted
        if arr[beg] <= arr[end]:
            return beg

        mid = (beg + end) // 2
        n = len(arr)

        prev = (mid - 1) % n
        nxt = (mid + 1) % n

        # Case 2: mid is the minimum element
        if arr[mid] <= arr[prev] and arr[mid] <= arr[nxt]:
            return mid

        # Case 3: decide direction
        if arr[mid] >= arr[beg]:
            beg = mid + 1
        else:
            end = mid - 1

#test cases 
print(find_rotations_binary([4,5,6,7,0,1,2]))  # 4
print(find_rotations_binary([1,2,3,4,5]))      # 0
print(find_rotations_binary([10]))             # 0
print(find_rotations_binary([3,4,5,1,2]))      # 3
print(find_rotations_binary([]))               # 0

    

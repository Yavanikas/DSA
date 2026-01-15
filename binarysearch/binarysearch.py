def binarysearch(arr,target):
    beg=0
    end=len(arr)-1

    while beg<=end:
        mid=(beg+end)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            beg=mid+1
        else:
            end=mid-1       
 
    return -1

arr = [1, 3, 5, 7, 9]
print(binarysearch(arr, 7))
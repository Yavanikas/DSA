'''if the list of sorted elements contain repeating elemnets we
need to find the first and last position of the element thats repeating'''

'''agenda 1: since the array is sorted we use binary search for it
   agenda 2: we use binary search twice 
   agenda 3: the time complexity of the program is O(nlogn)'''

def findpos(arr,target,firstpos):
    beg,end=0,(len(arr)-1)
    pos=-1
    while beg<=end:
        mid=(beg+end)//2

        if arr[mid]==target:
            pos=mid
            if firstpos:
              end =  mid-1
            else:
              beg = mid+1
        elif arr[mid]<target:
            beg=mid+1
        else:
            end=mid-1

    return pos 
#test case 1
arr = [5,7,7,8,8,8,10]

first = findpos(arr, 8, True)
last = findpos(arr, 8, False)

print(first, last)

#test case 2
print(findpos([1,2,3,4], 5, True))   # -1


        
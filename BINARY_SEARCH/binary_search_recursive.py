# RECURSIVE APPROACH:
def binary_search(arr,start,end,n):
    
    mid = (start+end)//2

    if start<=end:
        if arr[mid]==n:
            return "yes"

        elif arr[mid]<n:
            return binary_search(arr,mid+1,end,n)

        else:
            return binary_search(arr,start,mid-1,n)

    return "no"
            
arr = [1,2,3,4,5,6,7]

print (binary_search(arr,0,len(arr)-1,8))

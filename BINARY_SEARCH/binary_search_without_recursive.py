def binary_search(arr,n):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2

    while start<=end:
        mid = (start+end)//2

        if arr[mid]==n:
            return "yes"

        elif arr[mid]<n:
            start = mid + 1

        else:
            end = mid-1

    return "no"
            
arr = [1,2,3,4,5,6,7]

print (binary_search(arr,0))



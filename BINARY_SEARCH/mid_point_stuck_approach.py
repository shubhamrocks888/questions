# MID-POINT STUCK APPROACH:
def binary_search(arr,n):
    start = 0
    end = len(arr)-1
    mid = (start+end)//2

    while mid >=start and mid<=end:
        if arr[mid]==n:
            return "yes"

        elif arr[mid]<n:
            mid = (mid+end)//2

        else:
            mid = (start+mid)//2

    return "no"
            
arr = [1,2,3,4,5,6,7]

print (binary_search(arr,1))



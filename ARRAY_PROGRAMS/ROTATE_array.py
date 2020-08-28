#Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements?

def left_rotate(arr,n):
    for i in range(n):
        left_rotate_by_one(arr,len(arr))

    return arr

def left_rotate_by_one(arr,n):
    temp = arr[0]

    for i in range(n-1):
        arr[i] = arr[i+1]

    arr[n-1] = temp

    return arr

arr = [1,2,3,4,5,6,7]

print (left_rotate(arr,2))

##Time complexity : O(n * d)
##Auxiliary Space : O(1)

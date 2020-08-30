            ##Merge Sort Algorithm
->Merge sort is one of the most efficient sorting algorithms. It works on the principle of Divide and Conquer.
->Merge sort repeatedly breaks down a list into several sublists until each sublist consists of a single element and
  merging those sublists in a manner that results into a sorted list.


A merge sort works as follows: 

##Top-down Merge Sort Implementation:
->The top-down merge sort approach is the methodology which uses recursion mechanism.
  It starts at the Top and proceeds downwards, with each recursive turn asking the same question such as “What is required to
  be done to sort the array?” and having the answer as, “split the array into two, make a recursive call, and merge the results.”,
  until one gets to the bottom of the array-tree.


#PYTHON-PROGRAM:
def merge(arr,start,mid,end):
    temp = [0] * (end-start+1)

    i,j,k = start,mid+1,0

    while (i<=mid and j<=end):

        if (arr[i]<=arr[j]):
            temp[k] = arr[i]
            i+=1
        else:
            temp[k] = arr[j]
            j+=1
        k+=1

    while (i<=mid):
        temp[k]=arr[i]
        k+=1
        i+=1

    while (j<=end):
        temp[k]=arr[j]
        k+=1
        j+=1

    for i in range(start,end+1):
        arr[i] = temp[i-start]
        

def mergesort(arr,start,end):

    if start<end:
        mid = (start+end)//2
        mergesort(arr,start,mid)
        mergesort(arr,mid+1,end)
        merge(arr,start,mid,end)

arr = [5,2,6,7,0,1,3]
mergesort(arr,0,len(arr)-1)

print (arr)
    

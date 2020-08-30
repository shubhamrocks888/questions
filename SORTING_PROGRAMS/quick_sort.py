##Quick Sort Algorithm
The name "Quick Sort" comes from the fact that, quick sort is capable of sorting a list of data elements significantly faster
(twice or thrice faster) than any of the common sorting algorithms. It is one of the most efficient sorting algorithms and is
based on the splitting of an array (partition) into smaller ones and swapping (exchange) based on the comparison with 'pivot'
element selected. Due to this, quick sort is also called as "Partition Exchange" sort. Like Merge sort, Quick sort also falls
into the category of divide and conquer approach of problem-solving methodology.


Technically, quick sort follows the below steps:
Step 1 − Make any element as pivot
Step 2 − Partition the array on the basis of pivot
Step 3 − Apply quick sort on left partition recursively
Step 4 − Apply quick sort on right partition recursively

#PYTHON-PROGRAM
def partition(arr,low,high):
    i = low-1
    pivot =arr[high]

    for j in range(low,high):

         if arr[j]<=pivot:
             i=i+1
             arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1



def quicksort(arr,low,high):

    if low<high:

        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)


arr = [5,6,2,7,0,1,3]

quicksort(arr,0,len(arr)-1)

print (arr)

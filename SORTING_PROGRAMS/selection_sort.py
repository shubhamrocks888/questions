##Selection Sort:

1. Selection sort is a simple comparison-based sorting algorithm.

2. We divide the array into two parts: sorted and unsorted.
   The left part is sorted subarray and the right part is unsorted subarray.
   Initially, sorted subarray is empty and unsorted array is the complete given array.

3. We perform the steps given below until the unsorted subarray becomes empty:

   Pick the minimum element from the unsorted subarray.
   Swap it with the leftmost element of the unsorted subarray.
   Now the leftmost element of unsorted subarray becomes a part (rightmost) of sorted subarray and
   will not be a part of unsorted subarray.

4. A selection sort works as follows: 
   Part of unsorted array

   Part of sorted array

   Leftmost element in unsorted array

   Minimum element in unsorted array


#PYTHON-PROGRAM:
def selection_sort(arr):

    for i in range(len(arr)):
        m= i
        for j in range (i+1,len(arr)):
            if arr[m]>arr[j]:
                m =j
        arr[i],arr[m] = arr[m],arr[i]

    return arr

arr = [5,2,6,7,1,0,3]  

print (selection_sort(arr))


'''
Total iterations = (n – 1) + (n – 2) + . . . + 1 = (n * (n – 1)) / 2 = (n2 – n) / 2

Therefore,

Time complexity: O(n2)

Space complexity: O(1)
'''
            
            

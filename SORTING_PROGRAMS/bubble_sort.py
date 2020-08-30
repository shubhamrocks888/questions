                    ##Bubble Sort
-> Bubble sort, also referred to as comparison sort, is a simple sorting algorithm that repeatedly goes through the list,
   compares adjacent elements and swaps them if they are in the wrong order.

-> This is the most simplest algorithm and inefficient at the same time.


##Explanation
Algorithm: We compare adjacent elements and see if their order is wrong (i.e a[i] > a[j] for 1 <= i < j <= size of array;
if array is to be in ascending order, and vice-versa). If yes, then swap them.





#PYTHON-PROGRAM:
def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            

    return arr
        
arr = [5,2,6,7,1,0,3]  
print (bubble_sort(arr))



-> This is used to identify whether the list is already sorted.
   When the list is already sorted (which is the best-case scenario), the complexity of bubble sort is only O(n).


##Worst case and Average case scenario:
In Bubble Sort, n-1 comparisons are done in the 1st pass, n-2 in 2nd pass, n-3 in 3rd pass and so on.
So, the total number of comparisons will be:
Sum = (n-1) + (n-2) + (n-3) + ..... + 3 + 2 + 1 
Sum = n(n-1)/2
Hence, the time complexity is of the order n2 or O(n2).


##Space Complexity of Bubble sort
The space complexity for the algorithm is O(1), because only a single additional memory space is required
i.e. for temporary variable used for swapping.

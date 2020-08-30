##          Insertion Sort Algorithm

->Insertion sort is the sorting mechanism where the sorted array is built having one item at a time.
->The array elements are compared with each other sequentially and then arranged simultaneously in some particular order.
->The analogy can be understood from the style we arrange a deck of cards.
->This sort works on the principle of inserting an element at a particular position, hence the name Insertion Sort.


##Insertion Sort works as follows:
->The first step involves the comparison of the element in question with its adjacent element.
  And if at every comparison reveals that the element in question can be inserted at a particular position,
  then space is created for it by shifting the other elements one position to the right and inserting the element at the suitable position.
  The above procedure is repeated until all the element in the array is at their apt position.




#PYTHON-PROGRAM:
def insertion_sort(arr):

    for i in range(1,len(arr)):
        value = arr[i]
        hole= i

        while (hole>0 and arr[hole-1]>value):
            arr[hole],arr[hole-1] = arr[hole-1],arr[hole]
            hole = hole-1

        

    return arr
            
arr = [4,5,3,2,0]  
print (insertion_sort(arr))

'''
Worst Case Time Complexity [ Big-O ]: O(n2)

Best Case Time Complexity [Big-omega]: O(n)

Average Time Complexity [Big-theta]: O(n2)
'''

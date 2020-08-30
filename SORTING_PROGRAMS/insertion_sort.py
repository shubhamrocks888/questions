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

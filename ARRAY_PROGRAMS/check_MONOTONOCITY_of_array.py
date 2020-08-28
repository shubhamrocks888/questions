# SELF-MADE

def monotonic(arr):

    if all([arr[i]-arr[i+1] >=0 for i in range(len(arr)-1)]):
        return "yes"

    elif all([arr[i]-arr[i+1] <=0 for i in range(len(arr)-1)]):
        return "yes"

    else:
        return "no"

##        OR            

'''
def isMonotonic(A): 
 
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

''' 


            
arr = [1,1,1,1,1,0]
print (monotonic(arr))

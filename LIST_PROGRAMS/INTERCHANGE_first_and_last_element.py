# SELF-MADE
def interchange(arr):
    l = len(arr)
    arr[0],arr[l-1] = arr[l-1],arr[0]
    return arr

arr = [12, 35, 9, 56, 24]
print (interchange(arr))

# APPROACH-1:

def interchange(arr):
    l = len(arr)
    arr[0],arr[-1] = arr[-1],arr[0]
    return arr

arr = [12, 35, 9, 56, 24]
print (interchange(arr))

# APPROACH-2:


def interchange(arr):
    first,*middle,last = arr

    arr = [last,*middle,first]
    return arr

arr = [12, 35, 9, 56, 24]
print (interchange(arr))

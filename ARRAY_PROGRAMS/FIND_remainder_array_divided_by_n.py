# STANDARD-APPROACH
First take a remainder or individual number like arr[i] % n. Then multiply the remainder with current result.
After multiplication, again take remainder to avoid overflow.
This works because of distributive properties of modular arithmetic. ( a * b) % c = ( ( a % c ) * ( b % c ) ) % c


def remainder(arr,n):
    x=1
    for i in arr:
        x = x*(i%n)

    return x%n

arr = [100,10,5,25,35,14] 

print (remainder(arr,11))



 

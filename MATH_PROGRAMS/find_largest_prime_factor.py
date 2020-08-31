##Python Program for Find largest prime factor of a number

def largest_prime(n):

    count=-1

    while n%2==0:
        if count!=2:
            count =2
        n = n/2

    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            if count!=i:
                count=i
            n = n/i

    if n>1:
        return n

    return count

print (largest_prime(21))

##Time complexity: O(sqrt(n)) 
##Auxiliary space: O(1) 


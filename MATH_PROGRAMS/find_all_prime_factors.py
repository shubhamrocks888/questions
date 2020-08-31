#SELF-APPRAOCH
##def find_prime(n):
##
##    while n%2==0:
##        print ('2',end=" ")
##        n = n/2
##
##    for i in range(3,(n//2),2):
##        while n%i==0:
##            print (i,end=" ")
##            n = n/i
##
##    if n>1:
##        print (n)
##
##
##find_prime(19)

#STANDARD -APPROACH;

'''reduce the for loop wih end = sqrt(n) with an interval of 2'''


def find_prime(n):

    while n%2==0:
        print ('2',end=" ")
        n = n/2

    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            print (i,end=" ")
            n = n/i

    if n>1:
        print (n)


find_prime(125)



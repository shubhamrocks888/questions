# SELF-MADE PROGRAM:

def fac(n):
    sum =1

    if n == 0 or n==1:
        return sum

    elif n==2:
        return 2

    else:
        for i in range(2,n+1):
            sum = sum*i

    return sum

print (fac(5))

# RECURSIVE PROGRAM:

def fac(n):

    if n==0 or n==1:
        return 1
    else:
        return (n)*fac(n-1)

print (fac(4)

#One line Solution (Using Ternary operator):

def fac(n):
    return 1 if n==0 or n==1 else n*fac(n-1)

print (fac(5))
        
     
       
        


        

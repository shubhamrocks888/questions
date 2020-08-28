#SELF-MADE PROGRAM:

def fibonacci(n):
    if n<0:
        return "Incorrect input"

    elif n==1 or n==2:
        return 1

    else:
        a=1
        b=0 

        for i in range(2,n):
            c =a+b
            b = a
            a = c

    return c

print (fibonacci(9))


#RECURSIVE  PROGRAM:

def fibonacci(n):
    if n<=0:
        return "Incorrect input"

    elif n==1:
        return 0

    elif n==2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)

print (fibonacci(9))

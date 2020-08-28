# SELF-MADE PROGRAM:

def check_prime(n):

    if n<2:
        return "No"
    else:
        for i in range(2,n):
            if n%i==0:
                return "no"
        else:
            return "yes"

print (check_prime(15))


# OPTIMIZED PROGRAM:

def check_prime(n):

    if n<2:
        return "No"
    else:
        for i in range(2,n//2):
            if n%i==0:
                return "no"
        else:
            return "yes"

print (check_prime(15))

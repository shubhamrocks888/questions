#SELF-MADE PROFRAM: 

def armstrong(n):
    sum=0
    l = list(str(n))

    for i in l:
        sum = sum + int(i)**len(l)

    if sum==n:
        return "yes"
    return "no"


print ( armstrong(1634) )

# C-TYPE PROGRAM:

def power(x,y):
    sum = 1

    for i in range(y):
        sum = sum*x

    return sum

def lengthh(n):
    l = 0

    while n!=0:
        l = l + 1
        n = n//10

    return l

def armstrong(n):
    l = lengthh(n)
    x = n
    sum = 0

    while x!=0:
        r = x%10
        sum = sum + power(r,l)
        x = x//10

    if sum==n:
        return "yes"
    return "no"

print ( armstrong(120) )






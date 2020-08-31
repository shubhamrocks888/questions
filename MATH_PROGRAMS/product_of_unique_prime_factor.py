##Python Program for Find largest prime factor of a number

def product_prime(n):

    product =1

    if n%2==0:
        product= product*2
        while n%2==0:
            n = n/2

    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            product = product*i
            while n%i==0:
                n = n/i

    if n>1:
        product = product*n

    return product

print (product_prime(15))




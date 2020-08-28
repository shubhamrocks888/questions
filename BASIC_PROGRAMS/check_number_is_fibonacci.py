#SELF-MADE
def check_fibonacci(n):
    if n<0:
        return "Incorrect input"

    elif n==0 or n==1 or n==2:
        return "yes"

    else:
        a=1
        b=0 

        for i in range(2,n):
            c =a+b
            if c>n:
                return "no"
            if c==n:
                return "yes"
            b = a
            a = c
        else:
            return "no"

print (check_fibonacci(144))


#STANDARD-TYPE:
First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ..

A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square.

def perfect_square(n):
    s = int(n**0.5)
    return s*s == n

def check_fibonacci(n):
    return perfect_square((5*(n**2))+4) or perfect_square((5*(n**2))-4)


print (check_fibonacci(4))


        'OR'

# python program to check if x is a perfect square 
import math 

# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
	s = int(math.sqrt(x)) 
	return s*s == x 

# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 

	# n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
	# is a perferct square 
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
	
# A utility function to test above functions 
for i in range(1,11): 
	if (isFibonacci(i) == True): 
		print i,"is a Fibonacci Number"
	else: 
		print i,"is a not Fibonacci Number "






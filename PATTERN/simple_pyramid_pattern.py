def pypart(n):
    for i in range(1,n+1):
        for i in range(i):
            print ('*',end=" ")
        print ()

pypart(5)

##Output:
* 
* * 
* * * 
* * * * 
* * * * *

##Another Approach:
    
def pypart(n):
    mylist = []
    for i in range(n+1):
        mylist.append("*"*i)
    x = "\n".join(mylist)
    print (x)

pypart(5)

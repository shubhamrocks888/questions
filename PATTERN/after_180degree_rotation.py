##        * 
##      * * 
##    * * * 
##  * * * * 
##* * * * * 

def pypart(n):
    k=n
    for i in range(1,n+1):
        k=k-1
        for j in range(k,0,-1):
            print (" ",end="")
        print ("*"*i,end="\n")

pypart(5)

##Output:
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * *

'''   

'''

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

'''


    
def numpat(n):
    for i in range(1,n+1):
        x=1
        for j in range(i):
            print (x,end=" ")
            x=x+1
        print (end="\n")

numpat(5)

    
    

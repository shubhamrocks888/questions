def numpat(n):
    x=1
    for i in range(1,n+1):
        for j in range(i):
            print (x,end=" ")
            x=x+1
        print (end="\n")

numpat(5)

'''

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15

'''

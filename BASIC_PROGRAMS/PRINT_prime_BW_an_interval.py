def prime (start,end):


    if start<2:
        start =2
        
    for i in range (start,end):

        for j in range(2,i):

            if i%j==0:
                break
        else:
            print (i)

prime (-8,10)

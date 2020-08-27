def CI(p,r,t):

    x = 1+(r/100)
    y = x**t
    a = p*y

    return a-p

print ( CI(10000,10.25,5) )
        

##ALTER (LINES REDUCES)
def CI(p,r,t):
    a = ((1+(r/100))**t)*p

    return a-p

print ( CI(10000,10.25,5) )
        

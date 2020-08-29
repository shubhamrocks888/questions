#SELF-MADE:

def second_largest(l):
    l = list(set(l))
    l.sort()
    return l[-2]

l = [100,100,100,90]

print (second_largest(l))

#this will work only if list in ascending order
def second_largest(l):
    x= l[0]
    y=x

    for i in range(1,len(l)):
        if x<l[i]:
            y=x
            x = l[i]
        

    return y

l = [90,100,100,100,100]

print (second_largest(l))



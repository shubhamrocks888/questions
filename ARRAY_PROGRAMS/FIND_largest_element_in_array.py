#SELF-MADE
def maximum(n):
    m = n[0]

    for i in range(1,len(n)):
        if m<n[i]:
            m = n[i]

    return m
            
print (maximum(l))



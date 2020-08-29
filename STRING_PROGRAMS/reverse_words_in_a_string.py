##Input : str = "geeks quiz practice code"
##Output : str = "code practice quiz geeks"
##

def reverse_words(s):
    l = s.split()
    l.reverse()
    return " ".join(l)

s = "geeks quiz practice code"
print (reverse_words(s))    

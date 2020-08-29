d = {}

d[0]=12
d[1]=23
d[2]=124
d[3]=72
d[4]=52
d[5]=62

##  1.Displaying the Keys Alphabetically

for i in sorted(d.keys()):
    print (i,end=" ")


##  2.Sorting the Keys and Values in Alphabetical Order using the Key.

for i in sorted(d.items()):
    print (i,end=" ")

##  3.Sorting the Keys and Values in Alphabetical Order using the Value.

for i in sorted(d.items(),key = lambda i: i[1]):
    print (i,end=" ")

#   4. Creates a sorted dictionary (sorted by key) 
from collections import OrderedDict 

dict = {'ravi':'10','rajnish':'9','sanjeev':'15','yash':'2','suraj':'32'} 
dict1 = OrderedDict(sorted(dict.items())) 
print(dict1) 



from collections import OrderedDict

##s = "geeksforgeeks"
##
##print (OrderedDict.fromkeys(s))
##OrderedDict([('g', None), ('e', None), ('k', None), ('s', None), ('f', None), ('o', None), ('r', None)])


# FIRST APPROACH:
def without_order(s):

    return "".join(set(s))

def with_order(s):

    return "".join(OrderedDict.fromkeys(s))

s = "geeksforgeeks"
print (without_order(s))
print (with_order(s))

#SECOND APPROACH (with order without using module)
def remove_duplicate(s):

    t = ""

    for i in s:
        if i not in t:
            t = t+i

    return t

print (remove_duplicate("geeksforgeeks"))
            

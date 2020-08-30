1.)    start<=end is the primary or must condition for binary search, without that condition
       loop will occur endlessly and this is the condition by which when loop leave the
       array indexes, it will point you out that the element is not there.

2.)    second condition is that dont play with start or end,play with mid, like:

        1. mid = start+1
        2. mid = end - 1

       



##Python Program for Tower of Hanoi

Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules: 

1) Only one disk can be moved at a time. 

2) Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a
disk can only be moved if it is the uppermost disk on a stack. 

3) No disk may be placed on top of a smaller disk.

##Note:
Transferring the top n-1 disks from source rod to Auxiliary rod can again be thought of as a fresh problem and can be solved in the same manner.
 

def tower_of_hanoi(n,source,destination,auxiliary):
    if n==1:
        print (f"Move disk {n} from {source} to {destination}")
        return

    tower_of_hanoi(n-1,source,auxiliary,destination)
    print (f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1,auxiliary,destination,source)


tower_of_hanoi(2,'A','B','C')

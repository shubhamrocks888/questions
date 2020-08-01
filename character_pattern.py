'''
A 
B B 
C C C 
D D D D 
E E E E E
'''

def charpat(n):
     x = ord('A')
     for i in range(1,n+1):
        for j in range(i):
            print (chr(x),end=" ")
        x = x+1
        print(end='\n')

charpat(5)

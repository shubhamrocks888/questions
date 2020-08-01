def charpat(n):
     x = ord('A')
     for i in range(1,n+1):
        for j in range(i):
            print (chr(x),end=" ")
            x = x+1
       
        print(end='\n')

charpat(5)

'''
A 
B C 
D E F 
G H I J 
K L M N O
'''

Input: list - ["geeks", "for", "geeks"]
       word = geeks, N = 2
Output: list - ["geeks", "for"]

Input: list - ["can", "you",  "can", "a", "can" "?"]
       word = can, N = 1
Output: list - ["you",  "can", "a", "can" "?"]



def remove_occurrences(l,word,pos):
    count = 0

    for i in range(len(l)):
        if l[i] == word:
            count +=1
        if count==pos:
            del(l[i]) '''OR'''  ##l.pop(i)
            return l


l = ["can", "you",  "can", "a", "can","?"]

print (remove_occurrences(l,"can",1))

    


'''
Given a string, the task is check if every vowel is present or not.
We consider a vowel to be present if it is present in upper case or lower case.
i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .


Examples :

Input : geeksforgeeks
Output : Not Accepted
All vowels except 'o' are not present

Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present

'''

#SELF-MADE:
def check_vowels(s):
    l = ['a','i','e','o','u']

    s = s.lower()

    for i in l:
        if i not in s:
            return "False"
    return "True"

print (check_vowels("ABeeIghiObhkUul"))

#ALTERNATE APPROACH:
def check(string): 
if len(set(string).intersection("AEIOUaeiou"))>=5: 
	return ('accepted') 
else: 
	return ("not accepted") 

#Driver code 
if __name__=="__main__": 
string="geeksforgeeks"
print(check(string)) 



        

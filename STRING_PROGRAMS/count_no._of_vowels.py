'''Input : GeeksforGeeks
Output : No. of vowels : 5

Input : Hello World
Output : No. of vowels :  3'''


#SELF-MADE:
def check_vowels(s):
    count = 0
    s = s.lower()
    l = ['a','i','e','o','u']

    for i in l:
        if s.count(i):
            count = count + s.count(i)

    return count

print (check_vowels("Hello World"))



#SAME APPROACH USING SET:

# Python3 code to count vowel in 
# a string using set 

# Function to count vowel 
def vowel_count(str): 
	
	# Initializing count variable to 0 
	count = 0
	
	# Creating a set of vowels 
	vowel = set("aeiouAEIOU") 
	
	# Loop to traverse the alphabet 
	# in the given string 
	for alphabet in str: 
	
		# If alphabet is present 
		# in set vowel 
		if alphabet in vowel: 
			count = count + 1
	
	print("No. of vowels :", count) 
	
# Driver code 
str = "GeeksforGeeks"

# Function Call 
vowel_count(str) 


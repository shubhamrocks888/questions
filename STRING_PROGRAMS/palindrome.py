#SELF-MADE:

def palindrome(s):
    return s==s[::-1]

print (palindrome("geeks"))


# ITERATIVE METHOD
'''Run a loop from starting to length/2 and check the first character to the last character of the string and
second to second last one and so on …. If any character mismatches, the string wouldn’t be a palindrome.'''


def palindrome(s):

    for i in range(len(s)//2):
        if s[i]!=s[-1-i]:
            return "no"

    return "yes"

print (palindrome("geeks"))

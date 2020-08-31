##Input : 11:21:30 PM
##Output : 23:21:30
##
##Input : 12:12:20 AM
##Output : 00:12:20

'''
FOUR CASES:
1. AM with 12
2. PM with 12
3. AM with others
4. PM with others
'''

##Python program to convert time from 12 hour to 24 hour format
def convert_time(s):

    if s[:2]=='12' and s[-2]=='A':
        return "00"+s[2:-2]

    elif s[-2]=='A':
        return s[::-2]

    elif s[:2]=='12' and s[-2]=='P':
        return "00"+s[2:-2]

    else:
        return str(int(s[:2])+12) + s[2:-2]

print (convert_time("12:05:45 PM"))

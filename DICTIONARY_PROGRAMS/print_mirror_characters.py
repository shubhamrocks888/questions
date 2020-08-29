def mirror_characters(s):

    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    d = dict(zip(original,reverse))

    x = ""
    for i in s:
        x = x + d[i]

    return x

print (mirror_characters("abcdef"))

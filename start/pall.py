def isPallindrom(s):
    str1=s
    s=s[::-1]
    if (str1 == s):
        return 0
    else:
        return 1




val=isPallindrom('nitin')
print(val)
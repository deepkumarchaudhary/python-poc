def searchString(s,char):
    index = 0
    print (s)
    print (char)
    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index
            index += 1
    return -1










str1='ABCABCTC'
subStr='TC'
#print(str1.find(subStr))
print('index of substring in main string is:', searchString(str1,subStr))



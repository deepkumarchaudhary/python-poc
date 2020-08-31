def string_splosion(str):
    #print (str[:1])
    result = ""
    # On each iteration, add the substring of the chars 0..i
    for i in range(len(str)):
        result = result + str[:i+1]
    #print (result)
    return result


string_splosion('Code') #→ 'CCoCodCode'
#string_splosion('abc') → 'aababc'
#string_splosion('ab') → 'aab'
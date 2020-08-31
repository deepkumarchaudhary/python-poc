def hello_name(name):
  print ('Hello'+' '+ name+'!')
  return "Hello" + ' ' + name + '!'


def make_abba(a, b):
    print(a+b+b+a)

def make_tags(tag, word):
    print ('<'+tag+'>'+word+'</'+tag+'>')
    return '<'+tag+'>'+word+'</'+tag+'>'

def extra_end(str):
    str = str[-2:]
    print (str)
    print(str+str+str) 

def first_two(str):
  if len(str) < 2:
    print (str)
    return str
  else:
    print(str[:2])
    return(str[:2])

def first_half(str):
    if len(str) % 2 == 0:
        halfindex = len(str) / 2
        print (str[:int(halfindex)])

def without_end(str):
    print (str[1:len(str)-1])    

def combo_string(a, b):
    if len(a) > len(b):
        print(b+a+b)
        return b+a+b
    else:
        print (a+b+a)
        return a+b+a

def left2(str):
    print(str)
    if len(str) < 2:
        return -1
    else:
        print(str[:2])
        print(str[2:len(str)])
        print(str[2:len(str)]+str[:2])

hello_name('Bob')
#hello_name('Bob') → 'Hello Bob!'
#hello_name('Alice') → 'Hello Alice!'
#hello_name('X') → 'Hello X!'

#make_abba('Hi', 'Bye') #→ 'HiByeByeHi'
make_abba('Yo', 'Alice') #→ 'YoAliceAliceYo'
#make_abba('What', 'Up') → 'WhatUpUpWhat'



make_tags('i', 'Yay')# → '<i>Yay</i>'
#make_tags('i', 'Hello')# → '<i>Hello</i>'
#make_tags('cite', 'Yay')# → '<cite>Yay</cite>'

extra_end('Hello') #→ 'lololo'
#extra_end('ab') → 'ababab'
#extra_end('Hi') → 'HiHiHi'


first_two('Hello') #→ 'He'
#first_two('abcdefg') → 'ab'
#first_two('ab') → 'ab'

first_half('WooHoo')# → 'Woo'
#first_half('HelloThere') → 'Hello'
#first_half('abcdef') → 'abc'

without_end('Hello') #→ 'ell'
#without_end('java') → 'av'
#without_end('coding') → 'odin'

#combo_string('Hello', 'hi')# → 'hiHellohi'
combo_string('hi', 'Hello')# → 'hiHellohi'
#combo_string('aaa', 'b') → 'baaab'


#left2('Hello') #→ 'lloHe'
#left2('java') #→ 'vaja'
left2('Hi') #→ 'Hi'
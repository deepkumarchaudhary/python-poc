def front_times(str, n):
  print (str)
  str=str[0:3]
  print (str)
  result = ""
  for i in range(n):
      result = result + str
  print (result)
  return (result)


front_times('Chocolate',3)
#front_times('Chocolate', 2) → 'ChoCho'
#front_times('Chocolate', 3) → 'ChoChoCho'
#front_times('Abc', 3) → 'AbcAbcAbc
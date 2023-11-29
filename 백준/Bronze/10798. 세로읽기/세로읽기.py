array = []
max_legnth = 0
for i in range(5):
  s = input()
  array.append(s)
  max_legnth= max(max_legnth,len(s))



for j in range(max_legnth):
  for i in range(5):
    if(j<len(array[i])):
      print(array[i][j],end="")

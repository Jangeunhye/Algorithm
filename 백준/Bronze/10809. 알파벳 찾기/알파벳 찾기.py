s = input()
array = [-1]*26
for i in s:
  for j in range(26):
    if(i == chr(j+97) and array[j]!=1):
      array[j]= s.find(i)

for i in array:
  print(i, end=" ")
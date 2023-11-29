s = input()
s = s.upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
array = []
for i in alphabet:
  array.append(s.count(i))

if (array.count(max(array))==1):
  index = array.index(max(array))
  print(alphabet[index])
else:
  print("?")
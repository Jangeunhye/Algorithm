s = input().upper()
alphabet = list(set(s))
array = []

for i in alphabet:
  array.append(s.count(i))


if array.count(max(array))>=2:
  print("?")
else:
  print(alphabet[array.index(max(array))])

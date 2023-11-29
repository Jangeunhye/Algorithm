word = input()
length = len(word)
check = 1
for i in range(length//2):
  if(word[i]==word[length-i-1]):
    continue
  else:
    check= 0
    break
print(check)
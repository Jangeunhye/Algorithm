n = int(input())
sum = 0
for i in range(n):
  word = input()
  word_set= set()
  last_letter = word[0]
  temp = True
  for j in word:
    if j not in word_set:
      word_set.add(j)
      last_letter = j
    elif j in word_set and j!=last_letter:
      temp= False
  if(temp==True):
    sum+=1
print(sum)
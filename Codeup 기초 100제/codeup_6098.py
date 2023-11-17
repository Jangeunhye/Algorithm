array = [[0]*11 for _ in range(11)]

for i in range(1,11):
  temp = list(map(int,input().split()))
  for j in range(1,11):
    array[i][j] = temp[j-1]
  
x, y = 2,2

while True:
  if array[x][y]==0:
    array[x][y]=9

    if (array[x][y+1]!=1):
      y= y+1
    elif (array[x+1][y]!=1):
      x = x+1
    else:
      break


  elif array[x][y]==2:
    array[x][y]=9
    break


for i in range(1,11):
  for j in range(1,11):
    print(array[i][j],end=" ")
  print()
h, w = map(int, input().split())
n = int(input())

array = [[0]*(w+1) for _ in range(h+1)]

for i in range(n):
  l,d,x,y = map(int, input().split())

  if d==1:
    #세로방향

    for j in range(x,x+l):
      array[j][y] = 1
  
  else:
    #가로방향
    for j in range(y,y+l):
      array[x][j]=1
  
for i in range(1,h+1):
  for j in range(1,w+1):
    print(array[i][j],end=" ")
  print()

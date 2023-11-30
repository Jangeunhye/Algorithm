n = int(input())
array = [[0 for _ in range(101)] for _ in range(101)]
for _ in range(n):
  x, y  = map(int, input().split())
  for i in range(y,y+10):
    for j in range(x, x+10):
      array[i][j]  = 1
sum = 0
for i in range(1,101):
  for j in range(1, 101):
    sum += array[i][j]

print(sum) 

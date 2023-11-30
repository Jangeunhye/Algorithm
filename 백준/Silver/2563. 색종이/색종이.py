n = int(input())
array= [[0]*100 for _ in range(100)]

for _ in range(n):
  x, y = map(int, input().split())
  for i in range(99-y,89-y,-1):
        for j in range(x, x+10):
            array[i][j] +=1

sum = 0
for i in range(100):
    for j in range(100):
        if (array[i][j]>=2):
            sum += (array[i][j]-1)

print(100*n-sum)
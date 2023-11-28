array = [0 for _ in range(30)]

for i in range(28):
  num = int(input())
  array[num-1] = num

for j in range(30):
  if array[j]==0:
    print(j+1, end=" ")
